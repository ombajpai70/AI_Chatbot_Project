from utils.intent import is_document_query
from utils.sql_classifier import is_sql_query

from services.general_chat import handle_general_chat
from services.document_chat import handle_document_query
from services.sql_agent import handle_sql_query


def route_question(question):

    # -----------------------------
    # SQL Query
    # -----------------------------

    if is_sql_query(question):

        print("\nRouting -> SQL Agent")

        return handle_sql_query(question)

    # -----------------------------
    # Document Query
    # -----------------------------

    if is_document_query(question):

        print("\nRouting -> Document RAG")

        return handle_document_query(question)

    # -----------------------------
    # General AI
    # -----------------------------

    print("\nRouting -> General Chat")

    return handle_general_chat(question)