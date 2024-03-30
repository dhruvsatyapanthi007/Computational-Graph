import networkx as nx
# from networkx.drawing.nx_agraph import pyplot_tree
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph


# # Create a NetworkX graph
# G = nx.Graph()

# print(dir(nx.drawing.nx_agraph))

# # Add edges to the graph
# G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (4, 9), (4, 10)])

# # Draw the tree
# pos = nx.drawing.nx_agraph.pyplot_tree(G, root=1)

# # Draw the graph
# nx.draw(G, pos, with_labels=True)

# # Show the plot
# plt.show()


G = nx.Graph()

# Add edges to the graph
edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (4, 9), (4, 10)]
for edge in edges:
    G.add_edge(edge[0], edge[1])

# Convert the graph to an AGraph object
A = to_agraph(G)

# Set the layout to 'dot'
A.layout('dot')

# Draw the tree
A.draw('tree.png')