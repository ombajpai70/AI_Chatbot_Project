from ollama import chat

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        break

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    print("Bot:", response["message"]["content"])