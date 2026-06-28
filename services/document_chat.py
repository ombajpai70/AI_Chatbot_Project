from ollama import chat
from sentence_transformers import SentenceTransformer
import faiss
import pickle
from config import OLLAMA_MODEL
from retriever.document import retrieve_document
from utils.memory import get_history
from utils.persona import get_persona
from utils.query_classifier import classify_query
from utils.metadata_filter import detect_target_documents
from utils.prompt_builder import build_document_prompt
from utils.citation_builder import build_citations
from utils.top_k_selector import get_top_k

print("Loading Embedding Model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading FAISS Index...")
index = faiss.read_index("vector_store/index.faiss")

print("Loading Chunks...")
with open("vector_store/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

#TOP_K = 5


def handle_document_query(question):
    top_k = get_top_k(question)
    print(f"Top K : {top_k}")
    query_type = classify_query(question)

    target_documents = detect_target_documents(question)

    print(f"\nQuery Type : {query_type}")
    print(f"Target Documents : {target_documents}")

    result = retrieve_document(
        question,
        chunks,
        model,
        index,
        top_k,
        target_documents
    )

    if not result["found"]:
        return "I couldn't find this information in the document."

    context = result["context"]
    matched_chunks = result["matched_chunks"]

    if result["exact"]:
        print("\nExact Match Found")
    else:
        print("\nSemantic Match Found")

    print("\n================ CONTEXT ================\n")

    for chunk in matched_chunks:

        print("=" * 60)
        print("Page :", chunk["page"])
        print("Similarity :", round(chunk["score"], 4))
        print(chunk["text"])

    print("\n=========================================\n")

    persona = get_persona()
    messages = build_document_prompt(persona)
    messages.extend(get_history())
    llm_question = question

    if query_type == "lookup":

      if question.strip().isdigit():

        llm_question = (
            f"Find complete details for invoice number {question} "
            f"using only the provided context."
        )
    messages.append(
        {
            "role": "user",
            "content": f"""
Context:

{context}

Question:

{llm_question}
"""
        }
    )
    print("\n================ PROMPT SENT TO LLM ================\n")
    print(messages[-1]["content"])
    print("\n====================================================\n")
    response = chat(
        model=OLLAMA_MODEL,
        messages=messages
    )

    assistant_message = response["message"]["content"]

    citations = build_citations(matched_chunks)

    return f"""{assistant_message}

    ----------------------------------
    Sources

    {citations}
    """