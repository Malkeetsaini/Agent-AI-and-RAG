import { Link }
from "react-router-dom";
import { AuthContext } from "../context/AuthContext";
import {
   useState,
   useContext
   } from "react";

export default function Navbar(){

  // const token =
  // localStorage.getItem(
  //   "token"
  // );

  const {
    token,
    logout
  } = useContext(AuthContext);

  return (

    <div>

      <h2>
        AI Shopping Agent
      </h2>

      <Link to="/">
        Home
      </Link>

      {" | "}

      {

        token ?

        (
          <>
            <Link to="/cart">
              Cart
            </Link>

            {" | "}

            <button
              onClick={logout}
            >
              Logout
            </button>
          </>
        )

        :

        (

          <>
            <Link to="/login">
              Login
            </Link>

            {" | "}

            <Link to="/register">
              Register
            </Link>
          </>

        )

      }

    </div>

  );
}