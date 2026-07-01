from database.schema_loader import load_schema

_schema_cache = None


def load_schema_cache():

    global _schema_cache

    if _schema_cache is None:

        print("Loading Schema Cache...")

        _schema_cache = load_schema()

    return _schema_cache