import axios from "axios";

const API = "http://localhost:8000";

export const sendMessage = async(message)=>{

    const token =
        localStorage.getItem("token");

    const response =
        await axios.post(

            `${API}/chat`,

            {
                message
            },

            {
                headers:{
                    Authorization:
                    `Bearer ${token}`
                }
            }
        );

    return response.data;
};