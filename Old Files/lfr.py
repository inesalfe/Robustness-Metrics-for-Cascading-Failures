from typing import Generic
import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.community import LFR_benchmark_graph
import numpy as np
from random import randint as rand
import random

# LFR_benchmark_graph(n, 
#                     tau1, 
#                     tau2, 
#                     mu, 
#                     average_degree=None, 
#                     min_degree=None, 
#                     max_degree=None, 
#                     min_community=None, 
#                     max_community=None, 
#                     tol=1e-07, 
#                     max_iters=500, 
#                     seed=None)

def lfr(n, tau1, tau2, mu, avg_k, min_c):

	G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=avg_k, min_community=int(min_c*n), seed=0, max_iters=100)
	G.remove_edges_from(nx.selfloop_edges(G))
	
	print("Nodes:", G.number_of_nodes(), "\nEdges:", G.number_of_edges())
	print("Average degree:", np.average([G.degree[i] for i in range(G.number_of_nodes())]))

	colors = [-1 for _ in G]
	c = 0
	for v in G:
		for node in G.nodes[v]["community"]:
			if colors[node] != -1:
				break
			colors[node] = c
		else:
			c += 1

	nx.set_node_attributes(G, {n:colors[n] for n in G.nodes()}, 'community')

	return G

# works: 
#    graph = lfr(5000, 3, 3, 0.2, 4, seed=1)
#    graph = lfr(5000, 3, 1.1, 0.15, 4, seed=1)

if __name__ == '__main__':
	tau2 = [1.7, 2.0, 1.1, 1.4]
	mu = [0.1, 0.15, 0.2, 0.12]
	min_c = [0.2, 0.25, 0.1, 0.15]

	it = 1;
	for tau2_it in tau2:
		for mu_it in mu:
			for min_c_it in min_c:
				print(it)
				it += 1
				try:
					graph = lfr(5000, 3, tau2_it, mu_it, 4, min_c_it)
					nx.write_gml(graph, "Simulations/graphs/lfr_%d.gml" % i)
					print("We did it!: ", tau2_it, mu_it, min_c_it)
					i += 1
					if i == 5:
						break
				except nx.ExceededMaxIterations:
					pass

