from database.connection import get_connection
from utils.sql_validator import validate_sql


def execute_query(sql):
    validation = validate_sql(sql)

    if not validation["valid"]:

      return {
        "success": False,
        "error": validation["reason"]
    }

    connection = None

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(sql)

        columns = [col[0] for col in cursor.description]

        rows = cursor.fetchall()

        result = []

        for row in rows:

            result.append(
                dict(zip(columns, row))
            )

        return {
            "success": True,
            "data": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()