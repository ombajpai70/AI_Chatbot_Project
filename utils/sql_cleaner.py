import re


def clean_sql(sql: str) -> str:

    sql = sql.strip()

    # Remove Markdown code block
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)

    # Remove "Here is the SQL:"
    sql = re.sub(
        r"^Here\s+is\s+the\s+SQL\s*:?",
        "",
        sql,
        flags=re.IGNORECASE
    )

    sql = sql.strip()

    return sql