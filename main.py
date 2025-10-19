from loaders.youtube_loader import load_youtube_video
from stores.vector_store import build_vector_store
from stores.graph_store import build_graph, get_relations_text
from llm.query_rewriter import rewrite_queries
from llm.chatbot_engine import build_system_prompt, ask_gemini
from utils.helpers import format_ts

def main():
    docs, meta = load_youtube_video()
    qdrant = build_vector_store(docs)
    graph = build_graph(docs)
    relations_text = get_relations_text(graph)

    while True:
        query = input("\nEnter your query (or 'exit'): ")
        if query.lower() in ["exit", "quit", "q"]:
            print(" Exiting TubeTalk Ai.")
            break

        rewritten = rewrite_queries(query)
        print(f" Rewritten Queries: {rewritten}")

        relevant_docs = [
            doc for q in rewritten for doc in qdrant.similarity_search(q, k=5)
        ]

        unique_docs = list({
            (doc.page_content, doc.metadata.get("start_seconds", "?")): doc
            for doc in relevant_docs
        }.values())

        print(f" Found {len(unique_docs)} unique relevant documents.")
        context_text = "\n".join([
            f"Time Stamp {format_ts(doc.metadata.get('start_seconds', 0))}: {doc.page_content}"
            for doc in unique_docs
        ])

        system_prompt = build_system_prompt(context_text, relations_text)
        answer = ask_gemini(system_prompt, query)
        print(f"\n AI said:\n{answer}\n")

if __name__ == "__main__":
    main()
