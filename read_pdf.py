from pypdf import PdfReader

reader = PdfReader("documents/invoice.pdf")

print("Total Pages:", len(reader.pages))

text = ""

for i, page in enumerate(reader.pages):
    print(f"Reading Page {i+1}")
    page_text = page.extract_text()

    if page_text:
        text += page_text
    else:
        print(f"Page {i+1} is empty.")

print("\nTotal Characters:", len(text))
print("\nFirst 1000 Characters:\n")
print(text[:500])
