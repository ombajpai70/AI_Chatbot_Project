from utils.sql_validator import validate_sql

queries = [

    "SELECT * FROM dual",

    "UPDATE emp SET sal=1000",

    "DELETE FROM emp",

    "DROP TABLE emp",

    "WITH x AS (SELECT * FROM dual) SELECT * FROM x"

]

for sql in queries:

    print("=" * 60)

    print(sql)

    print(validate_sql(sql))