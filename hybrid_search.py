import re


def exact_search(question, chunks):

    question = question.upper().strip()

    # Extract invoice/GRN/CN number etc.
    tokens = re.findall(r"[A-Z]*\d+", question)

    if tokens:
        search_terms = tokens
    else:
        search_terms = [question]

    for chunk in chunks:

        text = chunk["text"]
        lines = text.splitlines()

        for i, line in enumerate(lines):

            line_upper = line.upper()

            if any(term in line_upper for term in search_terms):

                start = max(0, i - 3)
                end = min(len(lines), i + 8)

                return {
                    "document": chunk["document"],
                    "page": chunk["page"],
                    "text": "\n".join(lines[start:end])
                }

    return None