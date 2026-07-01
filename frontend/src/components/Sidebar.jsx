import { FaPlus, FaHistory } from "react-icons/fa";
import { Upload } from "lucide-react";
function Sidebar({ messages, setMessages }) {
    return (
        <div className="sidebar">

            <h2> ERP AI</h2>

            <button
                onClick={() => setMessages([])}
            >
                <FaPlus />
                New Chat
            </button>

            <button
                onClick={() => alert("Coming Soon")}
            >
                <FaHistory />
                History
            </button>
            <button>
                <Upload size={18} />
                Upload PDF
            </button>

        </div>
    );
}

export default Sidebar;