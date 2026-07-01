FOLLOWUP_WORDS = [

    "also",
    "only",
    "that",
    "those",
    "them",
    "it",
    "same",
    "above",
    "previous",
    "again",
    "customer",
    "amount",
    "date",
    "sort",
    "order",
    "descending",
    "ascending"

]


def is_followup(question):

    question = question.lower()

    return any(word in question for word in FOLLOWUP_WORDS)