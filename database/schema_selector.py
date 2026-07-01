def select_relevant_schema(schema, question):

    question = question.lower()

    selected_schema = {}

    for owner, tables in schema.items():

        for table_name, columns in tables.items():

            table_lower = table_name.lower()

            # Match table name
            if table_lower in question:

                selected_schema.setdefault(owner, {})
                selected_schema[owner][table_name] = columns
                continue

            # Match column names
            for column in columns:

                if column.lower() in question:

                    selected_schema.setdefault(owner, {})
                    selected_schema[owner][table_name] = columns
                    break

    # If nothing matched
    if not selected_schema:
        return schema

    return selected_schema