import re


ALLOWED_COMMANDS = [
    "SELECT",
    "WITH"
]

BLOCKED_COMMANDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "MERGE",
    "CREATE",
    "GRANT",
    "REVOKE",
    "COMMIT",
    "ROLLBACK"
]


def validate_sql(sql: str):

    sql = sql.strip()

    first_word = re.split(r"\s+", sql)[0].upper()

    if first_word in BLOCKED_COMMANDS:

        return {
            "valid": False,
            "reason": f"{first_word} statements are not allowed."
        }

    if first_word not in ALLOWED_COMMANDS:

        return {
            "valid": False,
            "reason": "Only SELECT statements are allowed."
        }

    return {
        "valid": True,
        "reason": ""
    }