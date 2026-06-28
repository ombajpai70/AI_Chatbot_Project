from ollama import chat
from utils.memory import (
    add_user,
    add_assistant,
    get_history
)
from utils.persona import get_persona
from utils.prompt_builder import build_general_prompt

def handle_general_chat(question):

    persona = get_persona()
    messages = build_general_prompt(persona)
    messages.extend(get_history())

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = chat(
        model="llama3.2",
        messages=messages
    )

    assistant_message = response["message"]["content"]

    add_user(question)
    add_assistant(assistant_message)

    return assistant_message