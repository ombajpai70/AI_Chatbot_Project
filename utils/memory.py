conversation_history = []

MAX_HISTORY = 10

def add_user(message):
    conversation_history.append({
        "role": "user",
        "content": message
    })

def add_assistant(message):
    conversation_history.append({
        "role": "assistant",
        "content": message
    })

def get_history():
    return conversation_history[-MAX_HISTORY:]

def clear_memory():
    conversation_history.clear()