def build_citations(matched_chunks):

    if not matched_chunks:
        return ""

    sources = []

    seen = set()

    for chunk in matched_chunks:

        source = (
            chunk["document"],
            chunk["page"]
        )

        if source in seen:
            continue

        seen.add(source)

        sources.append(
            f"- {chunk['document']} (Page {chunk['page']})"
        )

    return "\n".join(sources)