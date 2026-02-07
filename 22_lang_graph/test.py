import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes (entities)
G.add_node("Kiran")
G.add_node("Python")
G.add_node("AI")

# Add edges (relationships)
G.add_edge("Kiran", "Python", relation="uses")
G.add_edge("Kiran", "AI", relation="learns")
G.add_edge("AI", "Python", relation="implemented_in")

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)
edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()