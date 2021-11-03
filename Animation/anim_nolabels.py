import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

model = 0
while True:
	try:
		model = int(input("Choose model (0 - BA; 1 - DMS): "))       
	except ValueError:
		print("Please enter 0, or 1:")
		continue
	else:
		if model >= 0 and model <= 1:
			break
		else:
			continue

criteria = 0
while True:
	try:
		criteria = int(input("Choose criteria (0, 1, 2 or 3): "))       
	except ValueError:
		print("Please enter an integer between 0 and 3:")
		continue
	else:
		if criteria >= 0 and criteria <= 3:
			break
		else:
			continue

def grouped(iterable, n):
	return zip(*[iter(iterable)]*n)

if model == 0:
	G = nx.read_gml("Animation/Graphs/ba2.gml", None)
	file_name = "Animation/Data/ba_%i.txt" % criteria
else:
	G = nx.read_gml("Animation/Graphs/dms2.gml", None)
	file_name = "Animation/Data/dms_%i.txt" % criteria

for node in G.nodes():
	G.nodes[node]['pos'] = G.nodes[node]['graphics']['x'], G.nodes[node]['graphics']['y']

pos = nx.get_node_attributes(G,'pos')

it_list_v = []
it_list_e = []
with open(file_name, 'r') as f:
	for line in f:
		words = line.split()
		if (len(words) == 0):
			it_list_e[it].append(-1)
			it_list_e[it].append(-1)
		elif (words[0] == 'it'):
			it = int(words[1])-1
			it_list_v.append([])
			it_list_e.append([])
		elif (len(words) == 1):
			it_list_v[it].append(int(words[0]))
		else:
			for word in words:
				it_list_e[it].append(int(word))

N = G.number_of_nodes()
E = G.number_of_edges()

untouched_edges = list(G.edges)
deleted_edges = []
marked_edges = []
untouched_vertices = list(G.nodes)
deleted_vertices = []
marked_vertices = []

if model == 0:
	name = "Animation/Figures/ba_%i" % criteria
else:
	name = "Animation/Figures/dms_%i" % criteria

bc = nx.betweenness_centrality(G)
for bc_key in bc:
	if (bc[bc_key] == 0):
		bc[bc_key] = 0.03

sizes = dict(bc)

cut = 1.1
xmax= cut*max(xx for xx,yy in pos.values())
ymax= cut*max(yy for xx,yy in pos.values())
xmin= cut*min(xx for xx,yy in pos.values())
ymin= cut*min(yy for xx,yy in pos.values())

fig_it = 1

fig = plt.figure(figsize=(15, 7))
ax=plt.gca()

nx.draw_networkx(G, pos=pos, nodelist = untouched_vertices, node_color = 'blue', edgelist = untouched_edges, edge_color = 'black', alpha = 1.0, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes.values()])

ax.autoscale()
plt.axis('equal')
plt.axis('off')
plt.margins(0.0)
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)

plt.show()
fig_name = name + "_%i.png" % fig_it
fig.savefig(fig_name + '', format='png')
fig_it = fig_it + 1

for i in range(it+1):

	for v in it_list_v[i]:
		untouched_vertices.remove(v)
		marked_vertices.append(v)

	for e1, e2 in grouped(it_list_e[i], 2):
		if ((e1, e2) != (-1, -1)):
			untouched_edges.remove((e1, e2))
			marked_edges.append((e1, e2))

	sizes1 = dict((k, bc[k]) for k in untouched_vertices)
	sizes2 = dict((k, bc[k]) for k in marked_vertices)
	sizes3 = dict((k, bc[k]) for k in deleted_vertices)

	fig = plt.figure(figsize=(15, 7))
	ax=plt.gca()
	nx.draw_networkx(G, pos=pos, nodelist = untouched_vertices, node_color = 'blue', edgelist = untouched_edges, edge_color = 'black', alpha = 1.0, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes1.values()])
	nx.draw_networkx(G, pos=pos, nodelist = marked_vertices, node_color = 'red', edgelist = marked_edges, edge_color = 'red', alpha = 1.0, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes2.values()])
	nx.draw_networkx(G, pos=pos, nodelist = deleted_vertices, node_color = 'grey', edgelist = deleted_edges, edge_color = 'grey', alpha = 0.2, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes3.values()])
	ax.autoscale()
	plt.axis('equal')
	plt.axis('off')
	plt.margins(0.0)
	plt.xlim(xmin,xmax)
	plt.ylim(ymin,ymax)
	plt.show()
	fig_name = name + "_%i.png" % fig_it
	fig.savefig(fig_name, format='png')
	fig_it = fig_it + 1

	for v in marked_vertices:
		deleted_vertices.append(v)

	marked_vertices.clear()

	for e in marked_edges:
		deleted_edges.append(e)

	marked_edges.clear()

	sizes1 = dict((k, bc[k]) for k in untouched_vertices)
	sizes3 = dict((k, bc[k]) for k in deleted_vertices)

	fig = plt.figure(figsize=(15, 7))
	ax=plt.gca()
	nx.draw_networkx(G, pos=pos, nodelist = untouched_vertices, node_color = 'blue', edgelist = untouched_edges, edge_color = 'black', alpha = 1.0, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes1.values()])
	nx.draw_networkx(G, pos=pos, nodelist = deleted_vertices, node_color = 'grey', edgelist = deleted_edges, edge_color = 'grey', alpha = 0.2, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes3.values()])
	ax.autoscale()
	plt.axis('equal')
	plt.axis('off')
	plt.margins(0.0)
	plt.xlim(xmin,xmax)
	plt.ylim(ymin,ymax)
	plt.show()
	fig_name = name + "_%i.png" % fig_it
	fig.savefig(fig_name, format='png')
	fig_it = fig_it + 1
