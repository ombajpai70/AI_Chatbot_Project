import re


def detect_persona(text):

    text = text.lower().strip()

    patterns = [
        r"act like (.+)",
        r"behave like (.+)",
        r"you are (.+)",
        r"become (.+)"
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

    return None