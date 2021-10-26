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

def lfr(n, tau1, tau2, mu, avg_k, seed=None):

    if (n < 3):
        raise nx.NetworkXError("Invalid value for n")

    G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=avg_k, min_community=int(0.05*n), seed=seed)
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

    # communities = {frozenset(G.nodes[v]["community"]) for v in G}
    # n_communities = len(communities)
    # print(communities, n_communities)
    # colors = [i for v in G for i in range(len(communities)) if v in communities[i]]
    # print(colors)
    # print(communities, n_communities)
    # print([G.nodes[v]["community"] for v in G])

    nx.draw_spring(G, with_labels=False, node_color=colors)
    plt.show()

    return G

if __name__ == '__main__':
    lfr(1000, 3, 2, 0.15, 4, seed=10)
	# n_graphs = 10
	# n = 5000
	# for i in range(n_graphs):
	# 	graph = dms(n, i)
	# 	nx.write_gml(graph, "graphs/dms_%i.gml" % i)
