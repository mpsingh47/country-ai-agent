from langgraph.graph import StateGraph
from app.state import AgentState

from app.nodes.parse import parse_query
from app.nodes.tool import fetch_country_data
from app.nodes.synthesize import generate_answer

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("parse", parse_query)
    builder.add_node("tool", fetch_country_data)
    builder.add_node("answer", generate_answer)

    builder.set_entry_point("parse")

    builder.add_edge("parse", "tool")
    builder.add_edge("tool", "answer")

    return builder.compile()

graph = build_graph()