def build_general_prompt(persona=None):

    messages = []

    messages.append(
        {
            "role": "system",
            "content": """
You are a helpful AI assistant.

Answer professionally.

Be concise.

Never invent facts.

If you don't know something, say so.
"""
        }
    )

    if persona:

        messages.append(
            {
                "role": "system",
                "content": f"""
You are also acting as a professional {persona}.

Remain in this role until changed.
"""
            }
        )

    return messages


def build_document_prompt(persona=None):

    messages = []

    messages.append(
        {
            "role": "system",
            "content": """
You are an AI assistant.

Rules:

1. Use ONLY the provided context.

2. Never use outside knowledge.

3. Never guess.

4. If the answer is unavailable reply exactly:

'I couldn't find this information in the document.'

5. Organize raw PDF text before answering.

6. Keep answers short and professional.
"""
        }
    )

    if persona:

        messages.append(
            {
                "role": "system",
                "content": f"""
You are also acting as a professional {persona}.

Remain in this role.
"""
            }
        )

    return messages