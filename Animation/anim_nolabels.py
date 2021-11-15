import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

model = 0
model_name = None
while True:
	try:
		model = int(input("Choose model (0 - BA; 1 - DMS; 2 - Other): "))       
	except ValueError:
		print("Please enter 0, 1 or 2:")
		continue
	else:
		if model >= 0 and model <= 2:
			break
		else:
			continue
	
if model == 2:
	model_name = input("Input File Name: ").strip()

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
elif model == 1:
	G = nx.read_gml("Animation/Graphs/dms2.gml", None)
	file_name = "Animation/Data/dms_%i.txt" % criteria
else:
	G = nx.read_gml("Animation/Graphs/" + model_name + ".gml", None)
	file_name = "Animation/Data/" + model_name + "_%i.txt" % criteria

# print(G.edges())

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

# print(G.nodes[4164]['pos'])
# for n in G.nodes:
# 	print(n)
N = G.number_of_nodes()
E = G.number_of_edges()

untouched_edges = list(G.edges)
marked_edges = []
untouched_vertices = list(G.nodes)
deleted_vertices = []
deleted_edges = []

if model == 0:
	name = "Animation/Figures/ba_%i" % criteria
elif model == 1:
	name = "Animation/Figures/dms_%i" % criteria
else:
	name = "Animation/Figures/" + model_name + "_%i" % criteria


cut = 1.1
xmax= cut*max(xx for xx,yy in pos.values())
ymax= cut*max(yy for xx,yy in pos.values())
xmin= cut*min(xx for xx,yy in pos.values())
ymin= cut*min(yy for xx,yy in pos.values())

fig_it = 1

fig = plt.figure(figsize=(15, 7))
ax=plt.gca()

n_color = [G.nodes[n]['graphics']['fill'] for n in G.nodes()]
# n_color = ["blue" for n in G.nodes()]
e_color = ["#A0A0A0" for _ in G.edges()]
l_widths = [0 for _ in G.nodes()]
n_alpha = [1.0 for _ in G.nodes()]
e_alpha = [1.0 for _ in G.edges()]
aux_range = [G.nodes[n]['graphics']['w'] for n in G.nodes()]
interp = interp1d([np.min(aux_range), np.max(aux_range)],[5, 300])
# interp2 = interp1d([np.min(aux_range), np.max(aux_range)],[0, 1])
# l_widths = [float(interp2(s)) for s in aux_range]
n_sizes = [float(interp(s)) for s in aux_range]
nx.draw_networkx(G, pos=pos, nodelist = untouched_vertices, node_color = n_color, alpha = 1.0, edgelist = untouched_edges, edge_color = e_color, with_labels=False, node_size=n_sizes, linewidths=l_widths)
ax = plt.gca() # to get the current axis
ax.collections[0].set_edgecolor("#101010") 
ax.autoscale()
plt.axis('equal')
plt.axis('off')
plt.margins(0.0)
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)

# plt.show()

fig_name = name + "_%i.png" % fig_it
fig.savefig(fig_name + '', format='png')
fig_it = fig_it + 1

for i in range(it+1):

	# marked nodes
	for v in it_list_v[i]:
		n_color[list(G.nodes).index(v)] = "black"

	# marked edges
	for e1, e2 in grouped(it_list_e[i], 2):
		if ((e1, e2) != (-1, -1)):
			try:
				e_color[untouched_edges.index((e1, e2))] = "black"
				marked_edges.append((e1, e2))
			except ValueError:
				e_color[untouched_edges.index((e2, e1))] = "black"
				marked_edges.append((e2, e1))

	fig = plt.figure(figsize=(15, 7))
	ax=plt.gca()

	nx.draw_networkx_nodes(G, pos=pos, nodelist = untouched_vertices, node_color = n_color, alpha = n_alpha, node_size=n_sizes, linewidths=l_widths)
	nx.draw_networkx_edges(G, pos=pos, edgelist = untouched_edges, edge_color = e_color, alpha = e_alpha, )
	ax = plt.gca() # to get the current axis
	ax.collections[0].set_edgecolor("#101010") 
	# nx.draw_networkx(G, pos=pos, nodelist = untouched_vertices, node_color = 'blue', edgelist = untouched_edges, edge_color = 'black', alpha = 1.0, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes1.values()])
	# nx.draw_networkx(G, pos=pos, nodelist = marked_vertices, node_color = 'red', edgelist = marked_edges, edge_color = 'red', alpha = 1.0, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes2.values()])
	# nx.draw_networkx(G, pos=pos, nodelist = deleted_vertices, node_color = 'grey', edgelist = deleted_edges, edge_color = 'grey', alpha = 0.2, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes3.values()])
	ax.autoscale()
	plt.axis('equal')
	plt.axis('off')
	plt.margins(0.0)
	plt.xlim(xmin,xmax)
	plt.ylim(ymin,ymax)
	# plt.show()
	fig_name = name + "_%i.png" % fig_it
	fig.savefig(fig_name, format='png')
	fig_it = fig_it + 1

	# deleted nodes
	for v in it_list_v[i]:
		deleted_vertices.append(v)
		l_widths[list(G.nodes).index(v)] = 0
		n_color[list(G.nodes).index(v)] = "grey"
		n_alpha[list(G.nodes).index(v)] = 0.2

	# deleted edges
	for e in marked_edges:
		deleted_edges.append(e)
		idx = untouched_edges.index(e)
		e_color[idx] = "grey"
		e_alpha[idx] = 0.2

	marked_edges.clear()


	fig = plt.figure(figsize=(15, 7))
	ax=plt.gca()
	nx.draw_networkx_nodes(G, pos=pos, nodelist = untouched_vertices, node_color = n_color, alpha = n_alpha, node_size=n_sizes, linewidths=l_widths)
	nx.draw_networkx_edges(G, pos=pos, edgelist = untouched_edges, edge_color = e_color, alpha = e_alpha)
	ax = plt.gca() # to get the current axis
	ax.collections[0].set_edgecolor("#101010") 
	# nx.draw_networkx(G, pos=pos, nodelist = untouched_vertices, node_color = 'blue', edgelist = untouched_edges, edge_color = 'black', alpha = 1.0, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes1.values()])
	# nx.draw_networkx(G, pos=pos, nodelist = deleted_vertices, node_color = 'grey', edgelist = deleted_edges, edge_color = 'grey', alpha = 0.2, with_labels=False, font_weight='bold', node_size=[v * 1500 for v in sizes3.values()])
	ax.autoscale()
	plt.axis('equal')
	plt.axis('off')
	plt.margins(0.0)
	plt.xlim(xmin,xmax)
	plt.ylim(ymin,ymax)
	# plt.show()
	fig_name = name + "_%i.png" % fig_it
	fig.savefig(fig_name, format='png')
	fig_it = fig_it + 1

if model == 2:
	G.remove_nodes_from(deleted_vertices)
	nx.write_gml(G, "Animation/Graphs/" + model_name + "_%i_final.gml" % criteria)
	# print(2.0*G.number_of_edges()/G.number_of_nodes())
