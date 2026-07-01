from ollama import chat

from config import OLLAMA_MODEL
from utils.sql_cleaner import clean_sql


def retry_sql(question, schema, previous_sql, error):

    messages = [

        {
            "role": "system",
            "content": """
You are an Oracle SQL expert.

The previous SQL failed.

Fix ONLY the SQL.

Rules:

1. Use only the provided schema.
2. Do not explain.
3. Return ONLY Oracle SQL.
4. Generate SELECT only.
"""
        },

        {
            "role": "user",
            "content": f"""
Question:

{question}

Schema:

{schema}

Previous SQL:

{previous_sql}

Oracle Error:

{error}

Generate corrected SQL.
"""
        }

    ]

    response = chat(
        model=OLLAMA_MODEL,
        messages=messages
    )

    return clean_sql(
        response["message"]["content"]
    )