import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

with open('data.txt') as f:
    lines = f.read().splitlines()

N = int(lines[0].split[1])
N_GRAPHS = int(lines[1].split[1])
IT = int(lines[2].split[1])
criteria = int(lines[3].split[1])
alphas = int(lines[4].split[1:11])

g_size = np.zeros(len(alphas))

l_it = 0
for net in range(N_GRAPHS):
	for a in range(len(alphas)):
		for it in range(IT):
			g_size[a] += lines[9+5*l_it].split[1]
			l_it += 1

g_size = g_size / (N*IT*N_GRAPHS)

print(g_size)
