from database.connection import get_connection


def load_schema():

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT owner,
                   table_name,
                   column_name
            FROM all_tab_columns
            WHERE owner IN (
                'SALES',
                'PURCHASE',
                'FINANCE',
                'INVENT'
            )
            ORDER BY owner,
                     table_name,
                     column_id

        """)

        schema = {}

        for owner, table, column in cursor.fetchall():

            owner = owner.upper()
            table = table.upper()
            column = column.upper()

            schema.setdefault(owner, {})
            schema[owner].setdefault(table, [])
            schema[owner][table].append(column)

        return schema

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()