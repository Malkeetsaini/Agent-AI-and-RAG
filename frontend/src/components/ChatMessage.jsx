import { addToCart }
from "../api/cartApi";

export default function ChatMessage({ message }) {

    const isUser =
        message.role === "user";

    return (

        <div
            style={{
                display: "flex",
                justifyContent:
                    isUser
                        ? "flex-end"
                        : "flex-start",
                marginBottom: "15px"
            }}
        >

            <div
                style={{
                    maxWidth: "85%",
                    padding: "12px",
                    borderRadius: "12px",
                    background:
                        isUser
                            ? "#DCF8C6"
                            : "#F5F5F5"
                }}
            >

                <div
                    style={{
                        whiteSpace: "pre-wrap"
                    }}
                >
                    {message.content}
                </div>

                {
                    message.type ===
                    "search_products"

                    &&

                    message.tool_result?.products

                    &&

                    (
                        <div
                            style={{
                                marginTop: "15px"
                            }}
                        >

                            {
                                message.tool_result.products.map(
                                    (product) => (

                                        <div
                                            key={
                                                product.product_id
                                            }
                                            style={{
                                                border:
                                                    "1px solid #ddd",
                                                borderRadius:
                                                    "10px",
                                                padding:
                                                    "10px",
                                                marginBottom:
                                                    "10px",
                                                background:
                                                    "#fff"
                                            }}
                                        >

                                            <img
                                                src={
                                                    product.image_url
                                                }
                                                alt={
                                                    product.title
                                                }
                                                style={{
                                                    width:
                                                        "100%",
                                                    height:
                                                        "150px",
                                                    objectFit:
                                                        "cover",
                                                    borderRadius:
                                                        "8px"
                                                }}
                                            />

                                            <h4>
                                                {
                                                    product.title
                                                }
                                            </h4>

                                            <p>
                                                Category:
                                                {" "}
                                                {
                                                    product.category
                                                }
                                            </p>

                                            <p>
                                                Match:
                                                {" "}
                                                {
                                                    (
                                                        product.similarity
                                                        * 100
                                                    ).toFixed(0)
                                                }
                                                %
                                            </p>

                                            <button

                                                 onClick={() =>
                                                        addToCart(
                                                            product.product_id
                                                        )
                                                    }
                                                style={{
                                                    width:
                                                        "100%",
                                                    padding:
                                                        "8px"
                                                }}
                                            >
                                                Add To Cart
                                            </button>

                                        </div>
                                    )
                                )
                            }

                        </div>
                    )
                }

            </div>

        </div>
    );
}