import pdfplumber
from parser import parse_credit_notes

text = ""

with pdfplumber.open("documents/invoice.pdf") as pdf:

    for page in pdf.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

records = parse_credit_notes(text)

print("Total Records :", len(records))

if records:
    print("\nFirst Record\n")
    print(records[0])
else:
    print("No records found.")

# -------------------------
# Search Function
# -------------------------

def search_credit_note(cn):

    cn = cn.strip().upper()

    for record in records:

        if record["credit_note"].upper() == cn:
            return record

    return None

# -------------------------
# Test Search
# -------------------------

while True:

    q = input("\nEnter Credit Note : ").strip()

    if q.lower() == "exit":
        break

    result = search_credit_note(q)

    if result:

        print("\n========== FOUND ==========\n")
        print("Credit Note :", result["credit_note"])
        print(result["text"])

    else:

        print("\nNot Found")