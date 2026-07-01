import pickle

from database.schema_loader import load_schema


def build_schema_cache():

    print("Loading database schema...")

    schema = load_schema()

    with open("vector_store/schema_cache.pkl", "wb") as f:
        pickle.dump(schema, f)

    print("Schema Cached Successfully.")

    total_tables = 0

    for owner in schema:
        total_tables += len(schema[owner])

    print(f"Schemas : {len(schema)}")
    print(f"Tables  : {total_tables}")


if __name__ == "__main__":
    build_schema_cache()