from langgraph.constants import END
from langgraph.graph import StateGraph

from agent.planner.agent import planner_agent
from agent.architect.agent import architect_agent
from agent.coder.agent import coder_agent
from agent.reviewer.agent import reviewer_agent
from agent.routers import route_coder, route_reviewer

# Initialize the StateGraph orchestrating dict state
graph = StateGraph(dict)

# Register the service agent nodes
graph.add_node("planner", planner_agent)
graph.add_node("architect", architect_agent)
graph.add_node("coder", coder_agent)
graph.add_node("reviewer", reviewer_agent)

# Set up graph transitions
graph.add_edge("planner", "architect")
graph.add_edge("architect", "coder")

graph.add_conditional_edges(
    "coder", route_coder, {"reviewer": "reviewer", "coder": "coder"}
)

graph.add_conditional_edges(
    "reviewer", route_reviewer, {"END": END, "coder": "coder"}
)

graph.set_entry_point("planner")

# Compile the graph workflow
agent = graph.compile()

if __name__ == "__main__":
    # Test run locally
    result = agent.invoke(
        {"user_prompt": "Build a colourful modern todo app in html css and js"},
        {"recursion_limit": 100},
    )

    print("\nFinal State:")
    print(result)