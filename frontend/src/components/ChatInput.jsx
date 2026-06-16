import { useState } from "react";

export default function ChatInput({
    onSend
}){

    const [message,setMessage] =
        useState("");

    const submit = ()=>{

        if(!message.trim())
            return;

        onSend(message);

        setMessage("");
    };

    return(

        <div
            style={{
                display:"flex",
                gap:"10px"
            }}
        >

            <input
                value={message}
                onChange={(e)=>
                    setMessage(
                        e.target.value
                    )
                }
                placeholder="Ask anything..."
                style={{
                    flex:1
                }}
            />

            <button
                onClick={submit}
            >
                Send
            </button>

        </div>
    );
}