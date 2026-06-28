import os
import pickle
import faiss
import numpy as np
import pdfplumber
from sentence_transformers import SentenceTransformer
from utils.metadata_index_builder import build_metadata_index

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    EMBEDDING_MODEL,
    INDEX_PATH,
    CHUNKS_PATH
)
from utils.metadata_extractor import extract_metadata
from services.document_manager import get_all_documents


def build_index():

    documents = get_all_documents()

    if not documents:
        print("No PDF found inside documents folder.")
        return

    print(f"\nFound {len(documents)} PDF(s)\n")

    chunks = []

    # ----------------------------
    # Read Every PDF
    # ----------------------------

    for pdf_file in documents:

        print(f"Reading : {pdf_file}")

        with pdfplumber.open(pdf_file) as pdf:

            for page_number, page in enumerate(pdf.pages, start=1):

                page_text = page.extract_text()

                if not page_text:
                    continue

                step = CHUNK_SIZE - CHUNK_OVERLAP

                for i in range(0, len(page_text), step):

                    chunk = page_text[i:i + CHUNK_SIZE]
                    metadata = extract_metadata(chunk)
                    chunks.append(
                        {
                            "chunk_id": len(chunks),
                            "document": os.path.basename(pdf_file),
                            "page": page_number,
                            "text": chunk,
                            "metadata": metadata,
                            "source": f"{os.path.basename(pdf_file)} | Page {page_number}"
                        }
                    )

    print(f"\nTotal Chunks : {len(chunks)}")

    # ----------------------------
    # Embedding Model
    # ----------------------------

    print("\nLoading Embedding Model...")

    model = SentenceTransformer(
        EMBEDDING_MODEL
    )

    print("Creating Embeddings...")

    embeddings = model.encode(
        [chunk["text"] for chunk in chunks],
        normalize_embeddings=True
    )

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )

    # ----------------------------
    # FAISS
    # ----------------------------

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    # ----------------------------
    # Save
    # ----------------------------

    faiss.write_index(
        index,
        INDEX_PATH
    )

    with open(CHUNKS_PATH, "wb") as f:

        pickle.dump(chunks, f)
    build_metadata_index(chunks)
    print("\nIndex Built Successfully.")
    print("Vectors :", index.ntotal)