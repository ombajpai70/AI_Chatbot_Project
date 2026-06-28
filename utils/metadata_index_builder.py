import pickle

from config import METADATA_INDEX_PATH


def build_metadata_index(chunks):

    metadata_index = {}

    for chunk in chunks:

        metadata = chunk.get("metadata", {})

        for value in metadata.values():

            if not value:
                continue

            value = str(value).upper()

            metadata_index.setdefault(value, []).append(
                chunk["chunk_id"]
            )

    with open(METADATA_INDEX_PATH, "wb") as f:
        pickle.dump(metadata_index, f)

    print("Metadata Index Built Successfully")