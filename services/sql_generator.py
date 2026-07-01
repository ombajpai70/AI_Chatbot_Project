from ollama import chat

from config import OLLAMA_MODEL
from database.schema_cache import load_schema_cache
from utils.sql_prompt_builder import build_sql_prompt
from utils.sql_cleaner import clean_sql
from database.schema_selector import select_relevant_schema
from utils.schema_filter import filter_schema


def generate_sql(question):

    schema = load_schema_cache()
    schema = filter_schema(schema, question)
    print("\n========== FILTERED SCHEMA ==========\n")

    for owner in schema:

        print(owner)

        for table in schema[owner]:

            print("  ", table)

    print("\n=====================================\n")
    schema = select_relevant_schema(
    schema,
    question
    )

    messages = build_sql_prompt(
        schema,
        question
    )

    print("\n================ SQL PROMPT ================\n")
    print(messages[-1]["content"])
    for message in messages:
        print(message["role"].upper())
        print(message["content"])
        print()
    print("\n============================================\n")

    response = chat(
        model=OLLAMA_MODEL,
        messages=messages
    )

    raw_sql = response["message"]["content"]

    print("\n============= RAW LLM RESPONSE =============\n")
    print(raw_sql)
    print("\n============================================\n")

    sql = clean_sql(raw_sql)

    return sql