import pdfplumber

pdf_path = "documents/invoice.pdf"

with pdfplumber.open(pdf_path) as pdf:

    print("Total Pages :", len(pdf.pages))

    # Page 136 (Python indexing 0 se hoti hai)
    page = pdf.pages[135]

    print("\nReading Page 136...\n")

    print("=" * 80)

    # Normal text
    text = page.extract_text()

    print(text)

    print("=" * 80)