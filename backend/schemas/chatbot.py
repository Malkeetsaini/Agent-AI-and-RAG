from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class AgentIntent:

    GENERAL_CHAT = "GENERAL_CHAT"

    PRODUCT_SEARCH = "PRODUCT_SEARCH"

    ADD_TO_CART = "ADD_TO_CART"

    VIEW_CART = "VIEW_CART"

    PLACE_ORDER = "PLACE_ORDER"