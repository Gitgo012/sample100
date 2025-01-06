import networkx as nx
import matplotlib.pyplot as plt

# Function to visualize the graph
def visualize_graph(graph, title):
    # Improved visualization with better spacing
    pos = nx.spring_layout(graph, k=0.5, iterations=50)  # Adjust spacing with k
    edge_labels = nx.get_edge_attributes(graph, "relation")
    
    plt.figure(figsize=(12, 8))  # Bigger size for better clarity
    nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color="red", font_size=8)
    plt.title(title, fontsize=14)
    plt.axis("off")
    plt.show()

# Sentences and identified entities
sentences = [
    "Jerry is a cat.",
    "Jerry was sitting on the sofa.",
    "Jerry is owned by Tom.",
    "Tom called Jerry.",
    "Jerry walked from the sofa to Tom.",
    "Tom gave milk to Jerry.",
    "Jerry drank the milk."
]

# Step 1: Simple Semantic Net (Ignoring Verbs)
simple_nodes = ["Jerry", "cat", "sofa", "Tom", "milk"]
simple_edges = [
    ("Jerry", "cat", "belongs to category"), # Jerry is a cat
    ("Jerry", "sofa", "associated with"),   # Jerry was sitting on the sofa
    ("Jerry", "Tom", "belongs to"),         # Jerry is owned by Tom
    ("Tom", "Jerry", "connected to"),       # Tom called Jerry
    ("Jerry", "milk", "connected to")       # Jerry drank the milk
]

# Create and visualize simple semantic net
simple_graph = nx.MultiDiGraph()
simple_graph.add_nodes_from(simple_nodes)
for u, v, r in simple_edges:
    simple_graph.add_edge(u, v, relation=r)

visualize_graph(simple_graph, "Simple Semantic Net (Ignoring Verbs)")

# Step 2: Reified Semantic Net (With Verbs Expanded)
reified_nodes = ["Jerry", "cat", "sofa", "Tom", "milk", "calling", "walking", "giving", "drinking"]
reified_edges = [
    ("Jerry", "cat", "is a"),                     # Jerry is a cat
    ("Jerry", "sofa", "was sitting on"),         # Jerry was sitting on the sofa
    ("Jerry", "Tom", "is owned by"),             # Jerry is owned by Tom
    ("Tom", "calling", "agent"),                 # Tom called Jerry (agent)
    ("calling", "Jerry", "object"),              # Tom called Jerry (object)
    ("walking", "Jerry", "agent"),               # Jerry walked (agent)
    ("walking", "sofa", "from"),                 # Jerry walked from the sofa
    ("walking", "Tom", "to"),                    # Jerry walked to Tom
    ("giving", "Tom", "giver"),                  # Tom gave some milk (giver)
    ("giving", "milk", "object"),                # Tom gave some milk (object)
    ("giving", "Jerry", "receiver"),             # Tom gave some milk to Jerry (receiver)
    ("drinking", "Jerry", "agent"),              # Jerry drank milk (agent)
    ("drinking", "milk", "object")               # Jerry drank milk (object)
]

# Create and visualize reified semantic net
reified_graph = nx.MultiDiGraph()
reified_graph.add_nodes_from(reified_nodes)
for u, v, r in reified_edges:
    reified_graph.add_edge(u, v, relation=r)

visualize_graph(reified_graph, "Reified Semantic Net (With Verbs Expanded)")