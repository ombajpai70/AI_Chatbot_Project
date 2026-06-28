import re


def analyze_query(question):

    question = question.lower()

    result = {
        "invoice": None,
        "credit_note": None,
        "grn": None,
        "po": None,
        "keywords": []
    }

    invoice = re.search(r"invoice\s*(?:no)?\s*([a-z0-9]+)", question)

    if invoice:
        result["invoice"] = invoice.group(1)

    credit = re.search(r"cn\d+", question)

    if credit:
        result["credit_note"] = credit.group()

    grn = re.search(r"grn\s*([0-9]+)", question)

    if grn:
        result["grn"] = grn.group(1)

    result["keywords"] = question.split()

    return result