def remove_duplicate_chunks(chunks):

    unique = []
    seen = set()

    for chunk in chunks:

        key = (
            chunk["document"],
            chunk["page"]
        )

        if key in seen:
            continue

        seen.add(key)
        unique.append(chunk)

    return unique