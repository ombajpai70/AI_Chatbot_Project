from utils.intent import is_document_query

from services.general_chat import handle_general_chat
from services.document_chat import handle_document_query


def route_question(question):

    if is_document_query(question):

        return handle_document_query(question)

    return handle_general_chat(question)