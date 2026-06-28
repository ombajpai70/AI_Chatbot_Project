import numpy as np
from utils.duplicate_remover import remove_duplicate_chunks
from hybrid_search import exact_search
from utils.retriever import filter_results
from utils.context_builder import build_context
from retriever.metadata_search import metadata_search
def retrieve_document(question, chunks, model, index, top_k, target_documents=None):
    """
    Retrieves relevant document context.

    Returns:
    {
        found: bool,
        exact: bool,
        context: str,
        matched_chunks: list
    }
    """

    # -------------------------------------------------
    # STEP 0 : Metadata Search
    # -------------------------------------------------

    metadata_chunks = metadata_search(question)

    if metadata_chunks:

        matched_chunks = []

        for chunk in metadata_chunks:

            matched_chunks.append(
                {
                    "document": chunk["document"],
                    "page": chunk["page"],
                    "score": 1.0,
                    "text": chunk["text"]
                }
            )

        context = build_context(matched_chunks)

        return {
            "found": True,
            "exact": True,
            "context": context,
            "matched_chunks": matched_chunks
        }
    # -------------------------------------------------
    # STEP 1 : Exact Search
    # -------------------------------------------------

    exact_result = exact_search(question, chunks)

    if exact_result:

        matched_chunks = [
            {
                "document": exact_result["document"],
                "page": exact_result["page"],
                "score": 1.0,
                "text": exact_result["text"]
            }
        ]

        return {
            "found": True,
            "exact": True,
            "context": exact_result["text"],
            "matched_chunks": matched_chunks
        }

    # -------------------------------------------------
    # STEP 2 : Semantic Search
    # -------------------------------------------------

    question_embedding = model.encode(
        [question],
        normalize_embeddings=True
    )

    distance, index_number = index.search(
        np.array(question_embedding, dtype=np.float32),
        top_k
    )

    context, matched_chunks = filter_results(
        chunks,
        index_number,
        distance,
        target_documents
    )
    matched_chunks = remove_duplicate_chunks(
    matched_chunks
    )
    if target_documents:

        matched_chunks = [
        chunk
        for chunk in matched_chunks
        if chunk.get("document") in target_documents
        ]

    context = build_context(matched_chunks)

    if len(matched_chunks) == 0:

        return {
            "found": False,
            "exact": False,
            "context": "",
            "matched_chunks": []
        }

    # -------------------------------------------------
    # STEP 3 : Return Retrieved Context
    # -------------------------------------------------

    return {
        "found": True,
        "exact": False,
        "context": context,
        "matched_chunks": matched_chunks
    }