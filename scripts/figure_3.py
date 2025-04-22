import networkx as nx
import matplotlib.pyplot as plt

adj = [[0, 1, 0], [1, 0, 1], [1, 0, 0]]
nodes = ['a', 'b', 'c']

G = nx.DiGraph()
G.add_nodes_from(nodes)

for i, u in enumerate(nodes):
    for j, v in enumerate(nodes):
        if adj[i][j]:
            G.add_edge(u, v)

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True, node_size=700)
plt.show()
