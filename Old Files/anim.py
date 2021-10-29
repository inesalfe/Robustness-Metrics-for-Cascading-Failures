import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)

G = nx.read_gml('../Data/net.gml', None)

it_list_v = []
it_list_e = []
with open('../Data/v_edges.txt', 'r') as f:
    for line in f:
        words = line.split()
        if (words[0] == 'it'):
        	it = int(words[1])-1
        	it_list_v.append([])
        	it_list_e.append([])
        elif (len(words) == 1):
        	it_list_v[it].append(int(words[0]))
        else:
        	for word in words:
        		it_list_e[it].append(int(word))

print(it+1)
print(it_list_v)
print(it_list_e)

N = G.number_of_nodes()
E = G.number_of_edges()

print(N)
print(E)

untouched_edges = list(G.edges)
deleted_edges = []
marked_edges = []
untouched_vertices = list(G.nodes)
deleted_vertices = []
marked_vertices = []

fig_it = 1

fig = plt.figure()
nx.draw_networkx(G, pos=nx.spring_layout(G, seed=10), nodelist = untouched_vertices, node_color = 'blue', edgelist = untouched_edges, edge_color = 'black', alpha = 1.0, with_labels=True, font_weight='bold')
plt.show()
name = "Figures/%i.png" % fig_it
fig.savefig(name, format='png')
fig_it = fig_it + 1

for i in range(it+1):

	for v in it_list_v[i]:
		untouched_vertices.remove(v)
		marked_vertices.append(v)

	for e1, e2 in grouped(it_list_e[i], 2):
		untouched_edges.remove((e1, e2))
		marked_edges.append((e1, e2))

	fig = plt.figure()
	nx.draw_networkx(G, pos=nx.spring_layout(G, seed=10), nodelist = untouched_vertices, node_color = 'blue', edgelist = untouched_edges, edge_color = 'black', alpha = 1.0, with_labels=True, font_weight='bold')
	nx.draw_networkx(G, pos=nx.spring_layout(G, seed=10), nodelist = marked_vertices, node_color = 'red', edgelist = marked_edges, edge_color = 'red', alpha = 1.0, with_labels=True, font_weight='bold')
	nx.draw_networkx(G, pos=nx.spring_layout(G, seed=10), nodelist = deleted_vertices, node_color = 'grey', edgelist = deleted_edges, edge_color = 'grey', alpha = 0.2, with_labels=True, font_weight='bold')
	plt.show()
	name = "Figures/%i.png" % fig_it
	fig.savefig(name, format='png')
	fig_it = fig_it + 1

	for v in marked_vertices:
		deleted_vertices.append(v)

	marked_vertices.clear()

	for e in marked_edges:
		deleted_edges.append(e)

	marked_edges.clear()

	fig = plt.figure()
	nx.draw_networkx(G, pos=nx.spring_layout(G, seed=10), nodelist = untouched_vertices, node_color = 'blue', edgelist = untouched_edges, edge_color = 'black', alpha = 1.0, with_labels=True, font_weight='bold')
	nx.draw_networkx(G, pos=nx.spring_layout(G, seed=10), nodelist = deleted_vertices, node_color = 'grey', edgelist = deleted_edges, edge_color = 'grey', alpha = 0.2, with_labels=True, font_weight='bold')
	plt.show()
	name = "Figures/%i.png" % fig_it
	fig.savefig(name, format='png')
	fig_it = fig_it + 1
