from ollama import chat

SYSTEM_PROMPT = {
    "role": "system",
    "content": """
You are OmBot.

Rules:
1. Follow user instructions.
2. Keep answers concise unless user asks for details.
3. If user changes your role, acknowledge briefly.
4. Do not give long lectures unless asked.
5. Explain step by step when teaching.
6. Be friendly and professional.
"""
}

conversation_history = [SYSTEM_PROMPT]
while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        break
    
    if user_message.lower() == "clear":
        conversation_history.clear()
        conversation_history.append(SYSTEM_PROMPT)
        print("Memory Cleared")
        continue
    # 1. User message memory me store
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # 2. Ollama ko poori history bhejna
    response = chat(
        model="llama3.2",
        messages=conversation_history[-20:]
    )

    assistant_message = response["message"]["content"]

    # 3. AI response memory me store
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    # 4. Output print
    print("Bot:", assistant_message)