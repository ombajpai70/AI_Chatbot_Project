from utils.memory import (
    clear_memory,
)
from utils.role_detector import detect_persona
from utils.persona import (
    set_persona,
    clear_persona,
)
from services.router import route_question
from config import (
    OLLAMA_MODEL,
    EMBEDDING_MODEL,
    TOP_K,
    INDEX_PATH,
    CHUNKS_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    SIMILARITY_THRESHOLD,
)

while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    if question.lower() == "clear":
        clear_memory()
        clear_persona()
        print("Memory Cleared")
        continue

    persona = detect_persona(question)

    if persona:
        set_persona(persona)
        print(f"\nPersona Set : {persona}")
        continue

    answer = route_question(question)

    print("\nAnswer:\n")
    print(answer)