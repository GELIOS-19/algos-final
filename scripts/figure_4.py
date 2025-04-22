import networkx as nx
import matplotlib.pyplot as plt
import random


n = 9
p_edge = 0.2
G = nx.gnp_random_graph(n, p_edge, directed=True, seed=42)
mapping = {i: f'v{i}' for i in G.nodes()}
G = nx.relabel_nodes(G, mapping)
nodes = list(G.nodes())

random.seed(42)
landmarks = random.sample(nodes, 4)

H = nx.DiGraph()
H.add_nodes_from(nodes)

for v in nodes:
    for r in landmarks:
        try:
            d_vr = nx.shortest_path_length(G, source=v, target=r)
            H.add_edge(v, r, weight=d_vr)
        except nx.NetworkXNoPath:
            pass
        try:
            d_rv = nx.shortest_path_length(G, source=r, target=v)
            H.add_edge(r, v, weight=d_rv)
        except nx.NetworkXNoPath:
            pass

pos = nx.circular_layout(G)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

nx.draw(G, pos, ax=ax1, with_labels=True, node_size=300, node_color='skyblue', arrowsize=10)
ax1.set_title('Original Graph G')
ax1.axis('equal')

nx.draw_networkx_nodes(H, pos, ax=ax2, node_size=300, node_color='lightgreen')
nx.draw_networkx_labels(H, pos, ax=ax2)
nx.draw_networkx_nodes(H, pos, ax=ax2, nodelist=landmarks, node_color='orange', node_size=400)
nx.draw_networkx_edges(H, pos, ax=ax2, arrowsize=10)
edge_labels = {(u, v): d['weight'] for u, v, d in H.edges(data=True)}
nx.draw_networkx_edge_labels(H, pos, ax=ax2, edge_labels=edge_labels)
ax2.set_title('Transformed Graph H')
ax2.axis('equal')

plt.tight_layout()
plt.show()
