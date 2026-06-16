import os

from google import genai
from google.genai import types

from backend.services.search_service import semantic_search
from backend.services.cart_service import (
    get_cart,
    add_to_cart
)

from backend.services.order_service import (
    create_order
)

from backend.services.memory_service import (
    get_memory,
    update_memory_if_needed
)

from backend.services.chat_history_service import (
    get_recent_messages,
    save_chat_message as save_chat
)

from backend.utils.prompt_builder import (
    build_prompt
)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# =====================================================
# TOOL DEFINITIONS
# =====================================================

tools = [
    types.Tool(
        function_declarations=[
            {
                "name": "search_products",
                "description": "Search products from product catalog",
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "query": {
                            "type": "STRING",
                            "description": "Product search query"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "view_cart",
                "description": "View user shopping cart",
                "parameters": {
                    "type": "OBJECT",
                    "properties": {}
                }
            },
            {
                "name": "add_to_cart",
                "description": "Add product to cart",
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "product_query": {
                            "type": "STRING"
                        },
                        "quantity": {
                            "type": "INTEGER"
                        }
                    },
                    "required": [
                        "product_query",
                        "quantity"
                    ]
                }
            },
            {
                "name": "place_order",
                "description": "Place order using items currently in cart",
                "parameters": {
                    "type": "OBJECT",
                    "properties": {}
                }
            }
        ]
    )
]


# =====================================================
# TOOL EXECUTOR
# =====================================================

def execute_tool(
    tool_name,
    args,
    db,
    user_id
):

    print(f"TOOL CALLED: {tool_name}")
    print(args)

    if tool_name == "search_products":

        if not args["query"] :
            return {
                "success": False,
                "message": "no query found"
            }

        products = semantic_search(
            query=args["query"],
            top_k=5
        )

        return {
            "products": products
        }

    elif tool_name == "view_cart":

        cart = get_cart(
            db,
            user_id
        )

        return {
            "cart": cart
        }

    elif tool_name == "add_to_cart":

        products = semantic_search(
            query=args["product_query"],
            top_k=1
        )

        if not products:

            return {
                "success": False,
                "message": "Product not found"
            }

        product_id = int(
            products[0]["product_id"]
        )

        result = add_to_cart(
            db,
            user_id,
            product_id,
            args["quantity"]
        )

        return {
            "success": True,
            "result": result
        }

    elif tool_name == "place_order":

        result = create_order(
            db,
            user_id
        )

        return {
            "success": True,
            "result": result
        }

    return {
        "success": False,
        "message": "Unknown tool"
    }


# =====================================================
# MAIN CHAT AGENT
# =====================================================

def chat_agent(
    db,
    user_id,
    message
):

     # 1. Load Summary Memory
    memory = get_memory(
        db,
        user_id
    )

    # 2. Load Recent Messages
    recent_messages = get_recent_messages(
        db,
        user_id,
        limit=10
    )

    # 3. Build Prompt
    prompt = build_prompt(
        memory.summary if memory else "",
        recent_messages,
        message
    )

    print("------------------------")
    print(prompt);
    print("------------------------")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=tools
        )
    )

    save_chat(
        db,
        user_id,
        "user",
        message
    )

    candidate = response.candidates[0]

    function_call = None

    for part in candidate.content.parts:

        if getattr(part, "function_call", None):

            function_call = part.function_call
            break

    # -------------------------------------------------
    # NORMAL CHAT
    # -------------------------------------------------

    if function_call is None:

        save_chat(
            db,
            user_id,
            "assistant",
            response.text
        )

        update_memory_if_needed(
            db,
            user_id
        )

        return {
            "type": "GENERAL_CHAT",
            "answer": response.text
        }

    # -------------------------------------------------
    # TOOL EXECUTION
    # -------------------------------------------------

    tool_name = function_call.name

    args = dict(function_call.args)

    tool_result = execute_tool(
        tool_name,
        args,
        db,
        user_id
    )

    # -------------------------------------------------
    # SEND TOOL RESULT BACK TO GEMINI
    # -------------------------------------------------

    final_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Content(
                role="user",
                parts=[
                    types.Part(
                        text=message
                    )
                ]
            ),
            types.Content(
                role="model",
                parts=[
                    types.Part(
                        function_call=function_call
                    )
                ]
            ),
            types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=tool_name,
                        response=tool_result
                    )
                ]
            )
        ]
    )

    save_chat(
        db,
        user_id,
        "assistant",
        final_response.text
    )

    update_memory_if_needed(
        db,
        user_id
    )

    return {
        "type": tool_name,
        "answer": final_response.text,
        "tool_result": tool_result
    }