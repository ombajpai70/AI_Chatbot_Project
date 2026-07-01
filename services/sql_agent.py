from services.sql_generator import generate_sql
from services.sql_retry import retry_sql

from database.executor import execute_query
from database.schema_cache import load_schema_cache
from utils.sql_memory import save_sql_context
from utils.sql_result_formatter import format_sql_result


def handle_sql_query(question):

    print("\nGenerating SQL...\n")

    sql = generate_sql(question)

    print("=" * 60)
    print(sql)
    print("=" * 60)

    result = execute_query(sql)

    # -------------------------------------
    # Retry once if SQL execution fails
    # -------------------------------------

    if not result["success"]:

        print("\nRetrying SQL...\n")

        schema = load_schema_cache()

        corrected_sql = retry_sql(
            question=question,
            schema=schema,
            previous_sql=sql,
            error=result["error"]
        )

        print("=" * 60)
        print(corrected_sql)
        print("=" * 60)

        result = execute_query(corrected_sql)

        if not result["success"]:

            return f"""
SQL Execution Failed

Original SQL

{sql}

----------------------------------------

Corrected SQL

{corrected_sql}

----------------------------------------

Oracle Error

{result["error"]}
"""

        sql = corrected_sql

    formatted_result = format_sql_result(
        result["data"]
    )
    save_sql_context(
    question,
    sql,
    formatted_result
    )
    return f"""
Generated SQL

{sql}

----------------------------------------

Result

{formatted_result}
"""