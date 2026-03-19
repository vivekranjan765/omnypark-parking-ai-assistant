import os
import chromadb
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer


class VectorDB:
    """
    A simple vector database wrapper using ChromaDB with HuggingFace embeddings.
    """

    def __init__(self, collection_name: str = None, embedding_model: str = None):
        """
        Initialize the vector database.

        Args:
            collection_name: Name of the ChromaDB collection
            embedding_model: HuggingFace model name for embeddings
        """
        self.collection_name = collection_name or os.getenv(
            "CHROMA_COLLECTION_NAME", "rag_documents"
        )
        self.embedding_model_name = embedding_model or os.getenv(
            "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
        )

        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(path="./chroma_db")

        # Load embedding model
        print(f"Loading embedding model: {self.embedding_model_name}")
        self.embedding_model = SentenceTransformer(self.embedding_model_name)


        try:
            self.client.delete_collection(self.collection_name)
        except Exception:
            pass

        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"description": "RAG document collection"},
        )

        print(f"Vector database initialized with collection: {self.collection_name}")

    def chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start = end

        return chunks
        

    def add_documents(self, documents: List) -> None:
        print(f"Processing {len(documents)} documents...")

        all_chunks = []
        all_ids = []
        all_metadata = []

        for doc_index, doc in enumerate(documents):
            content = doc["content"]
            metadata = doc["metadata"]

            chunks = self.chunk_text(content)

            for chunk_index, chunk in enumerate(chunks):
                chunk_id = f"doc_{doc_index}_chunk_{chunk_index}"

                all_chunks.append(chunk)
                all_ids.append(chunk_id)
                all_metadata.append(metadata)

        # Create embeddings
        print("Creating embeddings...")
        embeddings = self.embedding_model.encode(all_chunks).tolist()

        # Store in ChromaDB
        self.collection.add(
            documents=all_chunks,
            embeddings=embeddings,
            metadatas=all_metadata,
            ids=all_ids
        )
        print(f"Added {len(all_chunks)} chunks to vector database")

    def search(self, query: str, n_results: int = 5) -> Dict[str, Any]:
        query_embedding = self.embedding_model.encode([query]).tolist()

        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        return results
