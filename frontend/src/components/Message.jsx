function Message({ role, text }) {

    return (

        <div>

            <strong>

                {role === "user" ? "You" : "AI"}

            </strong>

            <p>{text}</p>

        </div>

    );

}

export default Message;