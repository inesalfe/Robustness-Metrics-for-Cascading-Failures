import networkx as nx
import numpy as np
from random import randint as rand
import random

def dms(n, seed=None):

	# The graph must have at least three nodes
	if (n < 3):
		raise nx.NetworkXError("Invalid value for n")

	G = nx.Graph()
	# Initial 3 nodes and 3 edges graph
	G.add_node(0)
	G.add_node(1)
	G.add_node(2)
	G.add_edge(0, 1)
	G.add_edge(1, 2)
	G.add_edge(2, 0)

	N = G.number_of_nodes()
	E = G.number_of_edges()

	random.seed(seed)

	# Connect a new node to a random chosen edge
	while(N < n):
		edge = list(G.edges())[rand(0, E-1)]
		G.add_node(N)
		G.add_edge(N, edge[0])
		G.add_edge(N, edge[1])
		N += 1
		E += 2

	return G

if __name__ == '__main__':
	# 10 Graphs
	n_graphs = 10
	# 5000 nodes
	n = 5000
	for i in range(n_graphs):
		graph = dms(n, i)
		nx.write_gml(graph, "Simulations/Graphs/dms_%i.gml" % i)
