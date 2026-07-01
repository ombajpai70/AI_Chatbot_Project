import ReactMarkdown from "react-markdown";

function ChatMessage({ role, text }) {
    return (
        <div className={role === "user" ? "user-message" : "bot-message"}>
            <div className="message-header">
                {role === "user" ? "🧑 You" : "🤖 Assistant"}
            </div>

            <div className="message-body">
                <ReactMarkdown>
                    {text}
                </ReactMarkdown>
            </div>
        </div>
    );
}

export default ChatMessage;