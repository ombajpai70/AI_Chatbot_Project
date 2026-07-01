import re

SQL_KEYWORDS = [

    "table",
    "record",
    "row",
    "column",

    "employee",
    "customer",
    "supplier",

    "invoice",
    "order",
    "purchase",
    "sales",
    "stock",
    "inventory",
    "vendor",

    "payment",
    "ledger",
    "balance",
    "amount",
    "salary",

    "voucher",
    "receipt",
    "quotation",
    "grn",
    "po",
    "cn",

    "show",
    "list",
    "find",
    "fetch",
    "display",
    "count",
    "sum",
    "average",
    "maximum",
    "minimum",
    "top"
]


def is_sql_query(question: str) -> bool:

    q = question.lower().strip()

    # Numeric lookup
    if re.search(r"\b\d{4,}\b", q):
        return True

    return any(keyword in q for keyword in SQL_KEYWORDS)