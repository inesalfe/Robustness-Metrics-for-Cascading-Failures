import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml('net.gml', None)

N = G.number_of_nodes()
E = G.number_of_edges()

print(N)
print(E)

color_map = []
for node in G:
	if node < 5:
		color_map.append('blue')
	else: 
		color_map.append('red')

nx.draw_networkx(G, node_color=color_map, with_labels=True, font_weight='bold')
plt.show()