from utils.persona import get_persona
from utils.sql_memory import get_sql_context
from utils.sql_followup_detector import is_followup

def build_sql_prompt(schema, question):

    messages = []

    messages.append(
        {
            "role": "system",
            "content": """
You are an Oracle SQL Expert.

Your task is to generate Oracle SQL queries.

Rules:

1. Use ONLY the provided schema.
2. Never invent tables.
3. Never invent columns.
4. Generate ONLY SELECT statements.
5. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, MERGE or TRUNCATE.
6. Never explain the SQL.
7. Return ONLY executable Oracle SQL.
8. Use table names exactly as provided.
9. Use column names exactly as provided.
10. If the question cannot be answered using the schema, return:

NOT_POSSIBLE
"""
        }
    )

    persona = get_persona()

    if persona:

        messages.append(
            {
                "role": "system",
                "content": f"""
Act as a professional {persona}.
"""
            }
        )

    schema_text = ""
    previous_context = ""

    if is_followup(question):

        memory = get_sql_context()

        if memory["question"]:

          previous_context = f"""

    Previous Question

    {memory["question"]}

    Previous SQL

    {memory["sql"]}

    Previous Result

    {memory["result"]}
    """

    for owner, tables in schema.items():

        schema_text += f"\nSchema : {owner}\n"

        for table, columns in tables.items():

            schema_text += f"\nTable : {table}\n"

            schema_text += "Columns:\n"

            for column in columns:

                schema_text += f"- {column}\n"

    messages.append(
    {
        "role": "user",
        "content": f"""
    Database Schema

    {schema_text}

    {previous_context}

    Current Question

    {question}

    Generate Oracle SQL.
    """
        }
    )

    return messages