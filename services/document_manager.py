import os

from config import PDF_PATH


def get_all_documents():

    documents = []

    folder = os.path.dirname(PDF_PATH)

    for file in os.listdir(folder):

        if file.lower().endswith(".pdf"):

            documents.append(
                os.path.join(folder, file)
            )

    return documents