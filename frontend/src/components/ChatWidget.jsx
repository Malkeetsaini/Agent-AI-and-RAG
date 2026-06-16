import {
    useState
} from "react";

import ChatInput
from "./ChatInput";

import ChatMessage
from "./ChatMessage";

import {
    sendMessage
}
from "../api/chatbotApi";

export default function ChatWidget(){

    const [messages,setMessages] =
        useState([]);

    const handleSend =
    async(message)=>{

        setMessages(prev=>[
            ...prev,
            {
                role:"user",
                content:message
            }
        ]);

        try{

            const apiResponse =
                await sendMessage(message);

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content: apiResponse.answer,
                    type: apiResponse.type,
                    tool_result:
                        apiResponse.tool_result || null
                }
            ]);

        }catch(error){

            console.log(error);
        }
    };

    return(

        <div
            style={{
                position:"fixed",
                right:"20px",
                bottom:"20px",

                width:"400px",
                height:"600px",

                background:"#fff",

                border:
                "1px solid #ddd",

                borderRadius:"15px",

                display:"flex",
                flexDirection:"column"
            }}
        >

            <div
                style={{
                    padding:"15px",
                    borderBottom:
                    "1px solid #ddd"
                }}
            >
                AI Shopping Agent
            </div>

            <div
                style={{
                    flex:1,
                    overflowY:"auto",
                    padding:"10px"
                }}
            >

                {

                    messages.map((msg,index)=>

                        <ChatMessage
                            key={index}
                            message={msg}
                        />
                    )

                }

            </div>

            <div
                style={{
                    padding:"10px"
                }}
            >
                <ChatInput
                    onSend={
                        handleSend
                    }
                />
            </div>

        </div>
    );
}