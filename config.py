OLLAMA_MODEL = "llama3.2"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

TOP_K = 5

SIMILARITY_THRESHOLD = 0.45

INDEX_PATH = "vector_store/index.faiss"

CHUNKS_PATH = "vector_store/chunks.pkl"

DOCUMENT_FOLDER = "documents"

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

PDF_PATH = "documents/invoice.pdf"

DEFAULT_TOP_K = 5

EXACT_SEARCH_TOP_K = 1

GENERAL_QUERY_TOP_K = 8

COMPARISON_QUERY_TOP_K = 10

METADATA_INDEX_PATH = "vector_store/metadata_index.pkl"

# ------------------------
# Oracle Database
# ------------------------

#DB_HOST = "10.0.2.15"
DB_HOST = "127.0.0.1"

DB_PORT = 1521

DB_SERVICE = "orcl"

DB_USER = "System"

DB_PASSWORD = "Manager1"