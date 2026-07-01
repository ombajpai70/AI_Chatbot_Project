import { useState } from "react";
import { SendHorizontal } from "lucide-react";

function ChatInput({ onSend }) {

    const [question, setQuestion] = useState("");

    function handleSend() {

        if (!question.trim()) return;

        onSend(question);
        setQuestion("");
    }

    return (

        <div className="chat-input-container">

            <textarea
                className="chat-input"
                placeholder="Ask anything..."
                value={question}
                rows={2}
                onChange={(e) => setQuestion(e.target.value)}
                onKeyDown={(e) => {

                    if (e.key === "Enter" && !e.shiftKey) {

                        e.preventDefault();
                        handleSend();

                    }

                }}
            />

            <button
                className="send-btn"
                onClick={handleSend}
            >
                <SendHorizontal size={20} />
            </button>

        </div>

    );

}

export default ChatInput;