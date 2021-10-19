import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

with open('../Data/data_4.txt') as f:
    lines = f.read().splitlines()

N = int(lines[0].split()[1])
N_GRAPHS = int(lines[1].split()[1])
IT = int(lines[2].split()[1])
criteria = int(lines[3].split()[1])
alphas = lines[4].split()[1:12]

a_it = np.zeros(len(alphas), dtype=int)
giant_c_avg = np.zeros(len(alphas))
giant_c_var = np.zeros(len(alphas))
giant_c_sizes = np.zeros((len(alphas), IT*N_GRAPHS))

l_it = 0
for net in range(N_GRAPHS):
	for a in range(len(alphas)):
		for it in range(IT):
			giant_c_sizes[a][a_it[a]] = float(lines[8+5*l_it].split()[1])
			l_it += 1
			a_it[a] += 1

giant_c_sizes = giant_c_sizes / N

for a in range(len(alphas)):
	giant_c_avg[a] = np.mean(giant_c_sizes[a])
	giant_c_var[a] = np.var(giant_c_sizes[a])

f1 = plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.scatter(alphas, giant_c_avg, color="blue")

plt.plot(alphas, giant_c_avg, color="blue")

plt.errorbar(alphas, giant_c_avg, giant_c_var, fmt='bo', markersize=5, capsize=5, ecolor="black", label="Edge Betweenness Centrality")

plt.xlim((-1.1, 11.1))
plt.ylim((-0.1, 1.1))

plt.grid()
plt.legend()
plt.xlabel(r'\textbf{$\alpha$}', fontsize=11)
plt.ylabel(r'\textbf{N\'/N}', fontsize=11)

plt.show()

f1.savefig("g_size_edges.png", bbox_inches='tight')
