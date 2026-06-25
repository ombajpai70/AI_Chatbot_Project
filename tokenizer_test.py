from transformers import AutoTokenizer
from sentence_transformers import SentenceTransformer

tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2"
)

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "hello"

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)
embedding = model.encode(text)

print("Original Text :", text)
print("Tokens        :", tokens)
print("Token IDs     :", token_ids)
print("Vector Length :", len(embedding))
print("First 10 Values:", embedding[:10])