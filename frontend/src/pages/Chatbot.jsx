import {
  useState
} from "react";

import {
  sendMessage as chat
} from "../api/chatbotApi";

export default function Chatbot() {

  const [message, setMessage] =
    useState("");

  const [messages, setMessages] =
    useState([]);

  const sendMessage =
    async () => {

      const res =
        await chat(message);

      setMessages([
        ...messages,

        {
          role: "user",
          text: message
        },

        {
          role: "assistant",
          text: res.answer
        }
      ]);

      setMessage("");
    };

  return (

    <div>

      {messages.map((m, i) => (

        <div key={i}>
          {m.role} :
          {m.text}
        </div>

      ))}

      <input
        value={message}
        onChange={(e) =>
          setMessage(
            e.target.value
          )
        }
      />

      <button
        onClick={
          sendMessage
        }
      >
        Send
      </button>

    </div>
  );
}