
# # # importing networkx
# # import networkx as nx
# # # importing matplotlib.pyplot
import matplotlib.pyplot as plt
 
# # g = nx.Graph()
 
# # # g.add_edge('a1', 'a2')
# # # g.add_edge(2, 3)
# # # g.add_edge(3, 4)
# # # g.add_edge('a1', 4)
# # # g.add_edge('a1', 4)
# # # g.add_edge(1, 5)

# # # nx.draw(g, with_labels = True, connectionstyle='arc3, rad = 0.1')
# # # plt.savefig("filename.png")



# # G = nx.MultiGraph()
# # G.add_node('a1')
# # G.add_node('3a')
# # key = G.add_edge('a1', '3a', weight = 2)
# # # key2 = G.add_edge('a1', '3a', weight = 3)

# # key2 = G.add_edge('3a', 'a1', weight = 3)
# # nx.draw(G, nx.spring_layout(G), with_labels = True, connectionstyle='arc3, rad = 0.2')
# # plt.savefig("filename.png")



# import matplotlib.pyplot as plt
# import networkx as nx
# # import my_networkx as my_nx

# G = nx.DiGraph()
# edge_list = [(1,2,{'w':'A1'}),(2,1,{'w':'A2'}),(2,3,{'w':'B'}),(3,1,{'w':'C'}),
#              (4,3,{'w':'D1'}),(4,3,{'w':'D2'}),(1,5,{'w':'E1'}),(5,1,{'w':'E2'}),
#              (3,5,{'w':'F'}),(5,4,{'w':'G'})]
# G.add_edges_from(edge_list)
# pos=nx.spring_layout(G,seed=5)
# fig, ax = plt.subplots()
# nx.draw_networkx_nodes(G, pos, ax=ax)
# nx.draw_networkx_labels(G, pos, ax=ax)


# fig.savefig("1.png", bbox_inches='tight',pad_inches=0)



# curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
# straight_edges = list(set(G.edges()) - set(curved_edges))
# nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges)
# arc_rad = 0.25
# nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges, connectionstyle=f'arc3, rad = {arc_rad}')
# fig.savefig("2.png", bbox_inches='tight',pad_inches=0)



# edge_weights = nx.get_edge_attributes(G,'w')
# curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
# straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
# # my_nx.my_draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=curved_edge_labels,rotate=False,rad = arc_rad)
# nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=straight_edge_labels,rotate=False)
# fig.savefig("3.png", bbox_inches='tight',pad_inches=0)



import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# # Add edges to the graph
# G.add_edge(1, 2)
# G.add_edge(1, 2)
# G.add_edge(1, 2)

# # Draw the graph
# # nx.draw(G, with_labels=True)
# nx.draw(G, with_labels = True, connectionstyle='arc3, rad = 0.1')
# plt.savefig("filename.png")


# Create a list of edges
pos = {1: (0, 0), 2: (1, 1)}
pos = nx.spring_layout(G)
edges = [(1, 2), (1, 2), (1, 2)]

# Draw the graph with multiple edges
plt.figure()
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=5)
nx.draw_networkx_nodes(G, pos, nodelist=[1,2], node_color='b')
nx.draw_networkx_labels(G, pos)

plt.show()