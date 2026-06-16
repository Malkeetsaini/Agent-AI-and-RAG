import axios from "axios";

const API =
"http://localhost:8000";

export const addToCart =
async (
 product_id
)=>{

 const token =
 localStorage.getItem(
  "token"
 );

 const res =
 await axios.post(

 `${API}/cart/add`,

 {
  product_id,
  quantity:1,
  user_id:2
 },

 {
  headers:{
   Authorization:
   `Bearer ${token}`
  }
 }

 );

 return res.data;
};

export const getCart = async () => {

    const token = localStorage.getItem("token");

    const response = await axios.get(
        `${API}/cart/2`,
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    return response.data;
};

export const removeFromCart = async (item_id) => {

    const token = localStorage.getItem("token");

    return axios.delete(
        `${API}/cart/remove/${item_id}`,
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );
};