def build_context(chunks):

    context = ""

    for chunk in chunks:

        context += (
            f"[{chunk['document']} | "
            f"Page {chunk['page']}]\n"
        )

        context += chunk["text"]

        context += "\n\n"

    return context.strip()