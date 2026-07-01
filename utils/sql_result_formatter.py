def format_sql_result(rows):

    if not rows:
        return "No records found."

    output = []

    for i, row in enumerate(rows, start=1):

        output.append(f"Record {i}")

        output.append("-" * 40)

        for key, value in row.items():

            label = key.replace("_", " ").title()

            output.append(f"{label} : {value}")

        output.append("")

    return "\n".join(output)