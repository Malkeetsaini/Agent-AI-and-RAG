import {
  useState,
  useContext
} from "react";

import { useNavigate } from "react-router-dom"

import {
  loginUser
} from "../api/authApi";

import {
  AuthContext
} from "../context/AuthContext";

export default function Login() {

  const {
    login
  } = useContext(
    AuthContext
  );

  const navigate = useNavigate();

  const [email,setEmail] =
    useState("");

  const [password,setPassword] =
    useState("");

  const submit =
    async () => {

      const res =
        await loginUser({
          email,
          password
        });

      login(
        res.access_token
      );

      navigate("/");
    };

  return (
    <div>

      <input
        placeholder="Email"
        onChange={(e)=>
          setEmail(
            e.target.value
          )
        }
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e)=>
          setPassword(
            e.target.value
          )
        }
      />

      <button
        onClick={submit}
      >
        Login
      </button>

    </div>
  );
}