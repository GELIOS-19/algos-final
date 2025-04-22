import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('C', 'A'), ('A', 'B'), ('C', 'B')])

pos = {'A': (1, 1), 'B': (1, 0), 'C': (0, 0)}

plt.figure(figsize=(4, 4))
nx.draw(G, pos, with_labels=True, arrows=True, arrowstyle='-|>', arrowsize=20, node_size=800)
plt.axis('off')
plt.show()
