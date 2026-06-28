import re

def parse_credit_notes(text):

    records = []

    # Credit Note No. se split
    parts = re.split(r"(Credit Note No\.\s*CN\d+)", text)

    current_record = None

    for part in parts:

        part = part.strip()

        if not part:
            continue

        # Agar naya Credit Note mila
        if part.startswith("Credit Note No."):

            if current_record:
                records.append(current_record)

            credit_note = part.split()[-1]

            current_record = {
                "credit_note": credit_note,
                "text": part
            }

        else:

            if current_record:
                current_record["text"] += "\n" + part

    if current_record:
        records.append(current_record)

    return records