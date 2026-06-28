from services.document_manager import get_all_documents

documents = get_all_documents()

print()

print("Documents Found")

print("-" * 40)

for doc in documents:
    print(doc)