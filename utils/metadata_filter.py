def detect_target_documents(question):

    q = question.lower()

    documents = []

    if "invoice" in q or "cn" in q or "grn" in q:
        documents.append("invoice.pdf")

    if "trigger" in q or "procedure" in q or "plsql" in q:
        documents.append("oracle.pdf")
        documents.append("plsql.pdf")

    if "purchase" in q:
        documents.append("purchase.pdf")

    if "sales" in q:
        documents.append("sales.pdf")

    return documents