import axios from "axios";

const API = "http://localhost:8000";

export const placeOrder = async () => {

    const token = localStorage.getItem("token");

    const response = await axios.post(
        `${API}/orders`,
        {"user_id": 2},
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    return response.data;
};