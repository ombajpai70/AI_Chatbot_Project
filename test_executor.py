from database.executor import execute_query

sql = """
SELECT *
FROM dual
"""

result = execute_query(sql)

print(result)