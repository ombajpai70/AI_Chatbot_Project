from pypdf import PdfReader

reader = PdfReader("documents/invoice.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text

# -------------------------
# Chunking
# -------------------------

chunk_size = 500

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0])

print("\nSecond Chunk:\n")
print(chunks[1])