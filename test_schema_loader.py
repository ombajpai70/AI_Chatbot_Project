from database.schema_cache import load_schema_cache

schema = load_schema_cache()

for owner in schema:

    print("=" * 50)
    print(owner)

    for table in schema[owner]:

        print(table)

        print(schema[owner][table][:5])