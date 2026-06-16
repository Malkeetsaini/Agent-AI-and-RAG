import { useEffect, useState } from "react";

import {
    getCart,
    removeFromCart
} from "../api/cartApi";

import {
    placeOrder
} from "../api/orderApi";

import Navbar from
"../components/Navbar";

export default function Cart() {

    const [cartItems, setCartItems] = useState([]);

    console.log(cartItems);

    const loadCart = async () => {

        try {

            const data = await getCart();

            setCartItems(data);

        } catch (error) {

            console.log(error);

        }
    };

    useEffect(() => {

        loadCart();

    }, []);

    const handleRemove = async (id) => {

        await removeFromCart(id);

        loadCart();
    };

    const handleOrder = async () => {

        try {

            const response =
                await placeOrder();

            alert(
                `Order Created #${response.id}`
            );

            loadCart();

        } catch (error) {

            console.log(error);

        }
    };

    const totalPrice =
        cartItems.reduce(
            (sum, item) =>
                sum +
                (
                    item.price *
                    item.quantity
                ),
            0
        );

    return (

        <div
            style={{
                padding: "20px"
            }}
        >

            <Navbar />

            <h1>
                Shopping Cart
            </h1>
            

            {

                cartItems.map(
                    (item) => (

                        <div
                            key={item.id}
                            style={{
                                border:
                                    "1px solid #ddd",
                                padding:
                                    "10px",
                                marginBottom:
                                    "10px"
                            }}
                        >

                            <h3>
                                {
                                    item.title
                                }
                            </h3>

                            <p>
                                Quantity:
                                {
                                    item.quantity
                                }
                            </p>

                            <p>
                                Price:
                                ₹
                                {
                                    item.price
                                }
                            </p>

                            <button
                                onClick={() =>
                                    handleRemove(
                                        item.cart_item_id
                                    )
                                }
                            >
                                Remove
                            </button>

                        </div>

                    )
                )

            }

            <hr />

            <h2>

                Total :

                ₹

                {
                    totalPrice
                }

            </h2>

            <button
                onClick={
                    handleOrder
                }
            >
                Place Order
            </button>

        </div>

    );
}