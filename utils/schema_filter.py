def filter_schema(schema, question):

    question = question.lower()

    filtered = {}

    for owner, tables in schema.items():

        for table_name, columns in tables.items():

            table = table_name.lower()

            if table in question:

                if owner not in filtered:
                    filtered[owner] = {}

                filtered[owner][table_name] = columns

                continue

            for column in columns:

                if column.lower() in question:

                    if owner not in filtered:
                        filtered[owner] = {}

                    filtered[owner][table_name] = columns

                    break

    if filtered:
        return filtered

    return schema