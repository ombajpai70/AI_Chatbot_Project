from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    return model.encode(text, convert_to_tensor=True)


def calculate_similarity(text1, text2):
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)

    return cos_sim(emb1, emb2).item()