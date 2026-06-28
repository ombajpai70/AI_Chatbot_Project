import pickle

from config import (
    CHUNKS_PATH,
    METADATA_INDEX_PATH
)

# -------------------------
# Load Metadata Index
# -------------------------

with open(METADATA_INDEX_PATH, "rb") as f:
    metadata_index = pickle.load(f)

# -------------------------
# Load Chunks
# -------------------------

with open(CHUNKS_PATH, "rb") as f:
    chunks = pickle.load(f)


def metadata_search(question):

    key = question.strip().upper()

    if key not in metadata_index:
        return None

    chunk_ids = metadata_index[key]

    matched_chunks = []

    for chunk in chunks:

        if chunk["chunk_id"] in chunk_ids:

            matched_chunks.append(chunk)

    return matched_chunks