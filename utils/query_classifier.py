import re


def classify_query(question):

    q = question.lower()

    if re.search(r"\binvoice\b|\bcn\d+\b|\bgrn\b|\bpo\b", q):
        return "lookup"

    if any(word in q for word in [
        "compare",
        "difference",
        "vs"
    ]):
        return "comparison"

    if any(word in q for word in [
        "summary",
        "summarize",
        "overview"
    ]):
        return "summary"

    if any(word in q for word in [
        "list",
        "show all",
        "find all"
    ]):
        return "filter"

    return "knowledge"