import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_weighted_edges_from([('s', 't', 11), ('s', 'k', 5), ('k', 't', 5)])

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')
plt.show()
