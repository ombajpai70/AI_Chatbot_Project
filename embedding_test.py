from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")

hello = model.encode("hello")
hi = model.encode("hi")
hey = model.encode("hey")
database = model.encode("database")

print("hello vs hi")
print(cos_sim(hello, hi))

print()

print("hello vs hey")
print(cos_sim(hello, hey))

print()

print("hello vs database")
print(cos_sim(hello, database))

hlo = model.encode("hlo")
helo = model.encode("helo")

print("hello vs hlo")
print(cos_sim(hello, hlo))

print()

print("hello vs helo")
print(cos_sim(hello, helo))