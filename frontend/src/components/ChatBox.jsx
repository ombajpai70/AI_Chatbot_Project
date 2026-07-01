import { useState, useEffect, useRef } from "react";

import ChatInput from "./ChatInput";
//import Message from "./Message";
import ChatMessage from "./ChatMessage";
import { askQuestion } from "../services/api";

function ChatBox({ messages, setMessages }) {

    // const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const bottomRef = useRef(null);
    async function sendMessage(question) {

        setMessages(prev => [
            ...prev,
            {
                role: "user",
                text: question
            }
        ]);

        setLoading(true);

        try {

            const answer = await askQuestion(question);

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    text: answer
                }
            ]);

        }
        catch (err) {

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    text: "ERROR : " + err.message
                }
            ]);

        }

        setLoading(false);

    }
    useEffect(() => {

        bottomRef.current?.scrollIntoView({
            behavior: "smooth"
        });

    }, [messages, loading]);
    return (
        <div className="chat-container">

            <div className="messages">

                {messages.map((msg, index) => (

                    <ChatMessage
                        key={index}
                        role={msg.role}
                        text={msg.text}
                    />

                ))}

                {loading && (

                    <ChatMessage
                        role="assistant"
                        text="⏳ Thinking..."
                    />

                )}

                <div ref={bottomRef}></div>

            </div>

            <ChatInput onSend={sendMessage} />

        </div>
    );
}
export default ChatBox;