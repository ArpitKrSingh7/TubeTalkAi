from langchain_neo4j import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
from config import LLM_GPT, NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

def build_graph(docs):
    graph = Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD,
        refresh_schema=False,
    )
    llm_transformer = LLMGraphTransformer(llm=LLM_GPT)

    print("Building graph from transcript (this may take a while)...")
    graph_documents = llm_transformer.convert_to_graph_documents(docs)
    graph.add_graph_documents(graph_documents, baseEntityLabel=True, include_source=True)
    print(" Graph successfully built and saved. ")
    return graph

def get_relations_text(graph):
    query = """
    MATCH (a)-[r]->(b)
    RETURN a.id AS source, type(r) AS rel, b.id AS target
    """
    relations = graph.query(query)
    return "\n".join(f"{r['source']} --{r['rel']}--> {r['target']}" for r in relations)
