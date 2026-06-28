import re

def is_document_query(question):

    question = question.upper()

    patterns = [

        r"CN\d+",
        r"GRN",
        r"INVOICE",
        r"INVOICE NO",
        r"CREDIT NOTE",
        r"ACCOUNT",
        r"VAT",
        r"CUSTOMER",
        r"AMOUNT",
        r"TOTAL",
        r"SALES",
        r"\b30\d{4}\b"
    ]

    for pattern in patterns:

        if re.search(pattern, question):
            return True

    return False