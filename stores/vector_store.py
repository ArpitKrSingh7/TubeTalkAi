from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

def build_vector_store(docs):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    qdrant = QdrantVectorStore.from_documents(
        docs,
        embeddings,
        url="http://localhost:6333",
        collection_name=f"yt_collection_{docs[0].metadata.get('source','unknown')}"
    )
    print("  Data added to Qdrant successfully. ")
    return qdrant
