from services.sql_generator import generate_sql

question = input("Question: ")

sql = generate_sql(question)

print("\nGenerated SQL:\n")
print(sql)