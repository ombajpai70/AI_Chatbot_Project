from ollama import chat
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# --------------------------
# STEP 1 : Read PDF
# --------------------------

reader = PdfReader("documents/invoice.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text

print("PDF Read Successfully")

# --------------------------
# STEP 2 : Chunking
# --------------------------

chunk_size = 500

chunks = []

for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i+chunk_size])

print("Total Chunks:", len(chunks))

# --------------------------
# STEP 3 : Load Embedding Model
# --------------------------

print("Loading Embedding Model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

# --------------------------
# STEP 4 : Convert Chunks to Embeddings
# --------------------------

embeddings = model.encode(
    chunks,
    normalize_embeddings=True
)

print("Embedding Shape:", embeddings.shape)

# --------------------------
# STEP 5 : Create FAISS Index
# --------------------------

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(np.array(embeddings, dtype=np.float32))

print("Vectors Stored:", index.ntotal)

# --------------------------
# STEP 6 : User Question
# --------------------------

question = input("\nAsk Question: ")

question_embedding = model.encode(
    [question],
    normalize_embeddings=True
)

# --------------------------
# STEP 7 : Search
# --------------------------
TOP_K=5
distance, index_number = index.search(
    np.array(question_embedding,dtype=np.float32),
    TOP_K
)

print("\nTop Matching Chunks\n")

context = ""

for i in index_number[0]:
    context += chunks[i]
    context += "\n\n"

response = chat(
    model="llama3.2",
    messages=[
        {
         "role": "system",
    "content": """
You are an AI assistant.

Use ONLY the provided context.

If the answer is not available in the context,
reply exactly:

'I couldn't find this information in the document.'

Do not guess.
"""
        },
        {
            "role": "user",
            "content": f"""
Context:

{context}

Question:

{question}
"""
        }
    ]
)

print("\nAnswer:\n")
print(response["message"]["content"])

for idx, dist in zip(index_number[0], distance[0]):
    print("=" * 60)
    print("Distance:", dist)
    print(chunks[idx])