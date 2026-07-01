import { useState } from "react";

import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import ChatBox from "../components/ChatBox";

import "../styles/home.css";

function Home() {

    const [messages, setMessages] = useState([]);

    return (

        <div className="layout">

            <Sidebar
                messages={messages}
                setMessages={setMessages}
            />

            <div className="main">

                <Header />

                <ChatBox
                    messages={messages}
                    setMessages={setMessages}
                />

            </div>

        </div>

    );

}

export default Home;