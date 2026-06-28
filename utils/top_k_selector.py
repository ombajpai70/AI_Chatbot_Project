from config import (
    DEFAULT_TOP_K,
    EXACT_SEARCH_TOP_K,
    GENERAL_QUERY_TOP_K,
    COMPARISON_QUERY_TOP_K
)
import re

def get_top_k(question: str) -> int:

    question = question.lower()
    # Pure numeric lookup (Invoice No, Voucher No, etc.)
    if re.fullmatch(r"\d{4,}", question.strip()):
      return EXACT_SEARCH_TOP_K

    # Exact lookup queries
    exact_keywords = [
        "invoice",
        "invoice no",
        "invoice number",
        "credit note",
        "cn",
        "grn",
        "voucher",
        "po",
        "order no"
    ]

    if any(keyword in question for keyword in exact_keywords):
        return EXACT_SEARCH_TOP_K

    # Comparison / analytical queries
    comparison_keywords = [
        "compare",
        "difference",
        "highest",
        "lowest",
        "maximum",
        "minimum",
        "top",
        "list",
        "all"
    ]

    if any(keyword in question for keyword in comparison_keywords):
        return COMPARISON_QUERY_TOP_K

    # General document questions
    return GENERAL_QUERY_TOP_K