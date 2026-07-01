_last_question = None
_last_sql = None
_last_result = None


def save_sql_context(question, sql, result):

    global _last_question
    global _last_sql
    global _last_result

    _last_question = question
    _last_sql = sql
    _last_result = result


def get_sql_context():

    return {
        "question": _last_question,
        "sql": _last_sql,
        "result": _last_result
    }


def clear_sql_context():

    global _last_question
    global _last_sql
    global _last_result

    _last_question = None
    _last_sql = None
    _last_result = None