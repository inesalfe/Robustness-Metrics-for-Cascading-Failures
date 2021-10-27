import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def check_user_input(input):
	try:
		val = int(input)
		if val == 0 or val == 1:
			return True
		return False
	except ValueError:
		return False

input_int = input("Please choose the model:\n0 - Barabasi Albert\n1 - DMS Minimal Model\n")
while check_user_input(input_int) == False:
	input_int = input("Invalid input, try again\n")

if int(input_int) == int(0):
	folder = "../Data/BA/"
else:
	folder = "../Data/DMS/"

file = "data_0.txt"

with open(folder + file) as f:
    lines = f.read().splitlines()

N = int(lines[0].split()[1])
N_GRAPHS = int(lines[1].split()[1])
IT = int(lines[2].split()[1])
criteria = int(lines[3].split()[1])
alphas = lines[4].split()[1:12]

a_it = np.zeros(len(alphas), dtype=int)
unc_pairs_avg_rand = np.zeros(len(alphas))
unc_pairs_var_rand = np.zeros(len(alphas))
unc_pairs_sizes_rand = np.zeros((len(alphas), IT*N_GRAPHS))

l_it = 0
for net in range(N_GRAPHS):
	for a in range(len(alphas)):
		for it in range(IT):
			unc_pairs_sizes_rand[a][a_it[a]] = float(lines[10+6*l_it].split()[1])
			l_it += 1
			a_it[a] += 1

unc_pairs_sizes_rand = unc_pairs_sizes_rand / (N*(N-1)/2)

for a in range(len(alphas)):
	unc_pairs_avg_rand[a] = np.mean(unc_pairs_sizes_rand[a])
	unc_pairs_var_rand[a] = np.var(unc_pairs_sizes_rand[a])

file = "data_1.txt"

with open(folder + file) as f:
	lines = f.read().splitlines()

N = int(lines[0].split()[1])
N_GRAPHS = int(lines[1].split()[1])
IT = int(lines[2].split()[1])
criteria = int(lines[3].split()[1])
alphas = lines[4].split()[1:12]

a_it = np.zeros(len(alphas), dtype=int)
unc_pairs_avg_bc = np.zeros(len(alphas))
unc_pairs_var_bc = np.zeros(len(alphas))
unc_pairs_sizes_bc = np.zeros((len(alphas), IT*N_GRAPHS))

l_it = 0
for net in range(N_GRAPHS):
	for a in range(len(alphas)):
		for it in range(IT):
			unc_pairs_sizes_bc[a][a_it[a]] = float(lines[10+6*l_it].split()[1])
			l_it += 1
			a_it[a] += 1

unc_pairs_sizes_bc = unc_pairs_sizes_bc / (N*(N-1)/2)

for a in range(len(alphas)):
	unc_pairs_avg_bc[a] = np.mean(unc_pairs_sizes_bc[a])
	unc_pairs_var_bc[a] = np.var(unc_pairs_sizes_bc[a])

file = "data_2.txt"

with open(folder + file) as f:
	lines = f.read().splitlines()

N = int(lines[0].split()[1])
N_GRAPHS = int(lines[1].split()[1])
IT = int(lines[2].split()[1])
criteria = int(lines[3].split()[1])
alphas = lines[4].split()[1:12]

a_it = np.zeros(len(alphas), dtype=int)
unc_pairs_avg_dg = np.zeros(len(alphas))
unc_pairs_var_dg = np.zeros(len(alphas))
unc_pairs_sizes_dg = np.zeros((len(alphas), IT*N_GRAPHS))

l_it = 0
for net in range(N_GRAPHS):
	for a in range(len(alphas)):
		for it in range(IT):
			unc_pairs_sizes_dg[a][a_it[a]] = float(lines[10+6*l_it].split()[1])
			l_it += 1
			a_it[a] += 1

unc_pairs_sizes_dg = unc_pairs_sizes_dg / (N*(N-1)/2)

for a in range(len(alphas)):
	unc_pairs_avg_dg[a] = np.mean(unc_pairs_sizes_dg[a])
	unc_pairs_var_dg[a] = np.var(unc_pairs_sizes_dg[a])

file = "data_3.txt"

with open(folder + file) as f:
    lines = f.read().splitlines()

N = int(lines[0].split()[1])
N_GRAPHS = int(lines[1].split()[1])
IT = int(lines[2].split()[1])
criteria = int(lines[3].split()[1])
alphas = lines[4].split()[1:12]

a_it = np.zeros(len(alphas), dtype=int)
unc_pairs_avg_cl = np.zeros(len(alphas))
unc_pairs_var_cl = np.zeros(len(alphas))
unc_pairs_sizes_cl = np.zeros((len(alphas), IT*N_GRAPHS))

l_it = 0
for net in range(N_GRAPHS):
	for a in range(len(alphas)):
		for it in range(IT):
			unc_pairs_sizes_cl[a][a_it[a]] = float(lines[10+6*l_it].split()[1])
			l_it += 1
			a_it[a] += 1

unc_pairs_sizes_cl = unc_pairs_sizes_cl / (N*(N-1)/2)

for a in range(len(alphas)):
	unc_pairs_avg_cl[a] = np.mean(unc_pairs_sizes_cl[a])
	unc_pairs_var_cl[a] = np.var(unc_pairs_sizes_cl[a])

f1 = plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.scatter(alphas, unc_pairs_avg_rand, color="blue")
plt.scatter(alphas, unc_pairs_avg_bc, color="red")
plt.scatter(alphas, unc_pairs_avg_dg, color="green")
plt.scatter(alphas, unc_pairs_avg_cl, color="magenta")

plt.plot(alphas, unc_pairs_avg_rand, color="blue")
plt.plot(alphas, unc_pairs_avg_bc, color="red")
plt.plot(alphas, unc_pairs_avg_dg, color="green")
plt.plot(alphas, unc_pairs_avg_cl, color="magenta")

plt.errorbar(alphas, unc_pairs_avg_rand, unc_pairs_var_rand, fmt='bo', markersize=5, capsize=5, ecolor="black", label="Random")
plt.errorbar(alphas, unc_pairs_avg_bc, unc_pairs_var_bc, fmt='ro', markersize=5, capsize=5, ecolor="black", label="Betweeness Centrality")
plt.errorbar(alphas, unc_pairs_avg_dg, unc_pairs_var_dg, fmt='go', markersize=5, capsize=5, ecolor="black", label="Degree")
plt.errorbar(alphas, unc_pairs_avg_cl, unc_pairs_var_cl, fmt='mo', markersize=5, capsize=5, ecolor="black", label="Clustering Coefficient")

plt.xlim((-1.1, 11.1))
plt.ylim((-0.1, 1.1))

plt.grid()
plt.legend()
plt.xlabel(r'\textbf{$\alpha$}', fontsize=11)
plt.ylabel(r'\textbf{Fraction of unconnected pairs of nodes}', fontsize=11)

plt.show()

fig_name = "unc_pairs_nodes_%i.png" % int(input_int)

f1.savefig(fig_name, bbox_inches='tight')
