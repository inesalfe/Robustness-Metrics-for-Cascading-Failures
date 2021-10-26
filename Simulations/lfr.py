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

    G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=avg_k, min_community=int(0.1*n), seed=seed)
    
    print("Nodes:", G.number_of_nodes(), "\nEdges:", G.number_of_edges())
    print("Average degree:", np.average([G.degree[i] for i in range(G.number_of_nodes())]))

    nx.draw(G, with_labels=False, font_weight='bold')
    plt.show()

    return G

if __name__ == '__main__':
    lfr(250, 3, 1.5, 0.1, 5)
	# n_graphs = 10
	# n = 5000
	# for i in range(n_graphs):
	# 	graph = dms(n, i)
	# 	nx.write_gml(graph, "graphs/dms_%i.gml" % i)
