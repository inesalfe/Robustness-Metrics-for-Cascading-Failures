import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

model = 0
while True:
	try:
		model = int(input("""Choose a model:
		0 - Barabasi Albert Model w/ <k> = 4;
		1 - DMS Minimal Model w/ <k> = 4;
		2 - Power Law Model w/ <k> = 2;
		3 - Power Law Model w/ <k> = 4;
		4 - Random Graph Model w/ <k> = 4;
		5 - Watts-Strogatz Model w/ <k> = 4;
		6 - Power Grid Network;
		7 - Internet Network):\n>>> """))       
	except ValueError:
		print("Please an integer between 0 and 7:")
		continue
	else:
		if model >=0 or model <=7:
			break
		else:
			continue

if model == 0:
	folder = "Data/BA/"
elif model == 1:
	folder = "Data/DMS/"
elif model == 2:
	folder = "Data/PL2/"
elif model == 3:
	folder = "Data/PL4/"
elif model == 4:
	folder = "Data/RAND/"
elif model == 5:
	folder = "Data/WS/"
elif model == 6:
	folder = "Data/PG/"
else:
	folder = "Data/INT/"

file = "data_0.txt"

with open(folder + file) as f:
    lines = f.read().splitlines()

if model == 2:
	N = [int(i) for i in lines[0].split()[1:]]
else:
	N = [int(lines[0].split()[1]) for i in range(10)]

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
			temp_n = N[net] - np.sum([int(i) for i in lines[5+6*l_it].split()[1:]])
			unc_pairs_sizes_rand[a][a_it[a]] = float(lines[10+6*l_it].split()[1]) / temp_n / (temp_n-1) * 2
			l_it += 1
			a_it[a] += 1

for a in range(len(alphas)):
	unc_pairs_avg_rand[a] = np.mean(unc_pairs_sizes_rand[a])
	unc_pairs_var_rand[a] = np.var(unc_pairs_sizes_rand[a])

file = "data_1.txt"

with open(folder + file) as f:
	lines = f.read().splitlines()

if model == 2:
	N = [int(i) for i in lines[0].split()[1:]]
else:
	N = [int(lines[0].split()[1]) for i in range(10)]

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
			temp_n = N[net] - np.sum([int(i) for i in lines[5+6*l_it].split()[1:]])
			unc_pairs_sizes_bc[a][a_it[a]] = float(lines[10+6*l_it].split()[1]) / temp_n / (temp_n-1) * 2
			l_it += 1
			a_it[a] += 1

for a in range(len(alphas)):
	unc_pairs_avg_bc[a] = np.mean(unc_pairs_sizes_bc[a])
	unc_pairs_var_bc[a] = np.var(unc_pairs_sizes_bc[a])

file = "data_2.txt"

with open(folder + file) as f:
	lines = f.read().splitlines()

if model == 2:
	N = [int(i) for i in lines[0].split()[1:]]
else:
	N = [int(lines[0].split()[1]) for i in range(10)]

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
			temp_n = N[net] - np.sum([int(i) for i in lines[5+6*l_it].split()[1:]])
			unc_pairs_sizes_dg[a][a_it[a]] = float(lines[10+6*l_it].split()[1]) / temp_n / (temp_n-1) * 2
			l_it += 1
			a_it[a] += 1

for a in range(len(alphas)):
	unc_pairs_avg_dg[a] = np.mean(unc_pairs_sizes_dg[a])
	unc_pairs_var_dg[a] = np.var(unc_pairs_sizes_dg[a])

file = "data_3.txt"

with open(folder + file) as f:
    lines = f.read().splitlines()

if model == 2:
	N = [int(i) for i in lines[0].split()[1:]]
else:
	N = [int(lines[0].split()[1]) for i in range(10)]

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
			temp_n = N[net] - np.sum([int(i) for i in lines[5+6*l_it].split()[1:]])
			unc_pairs_sizes_cl[a][a_it[a]] = float(lines[10+6*l_it].split()[1]) / temp_n / (temp_n-1) * 2
			l_it += 1
			a_it[a] += 1

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

plt.errorbar(alphas, unc_pairs_avg_rand, np.sqrt(unc_pairs_var_rand), fmt='bo', markersize=5, capsize=5, ecolor="black", label="Random")
plt.errorbar(alphas, unc_pairs_avg_bc, np.sqrt(unc_pairs_var_bc), fmt='ro', markersize=5, capsize=5, ecolor="black", label="Betweeness Centrality")
plt.errorbar(alphas, unc_pairs_avg_dg, np.sqrt(unc_pairs_var_dg), fmt='go', markersize=5, capsize=5, ecolor="black", label="Degree")
plt.errorbar(alphas, unc_pairs_avg_cl, np.sqrt(unc_pairs_var_cl), fmt='mo', markersize=5, capsize=5, ecolor="black", label="Clustering Coefficient")

plt.xlim((-1.1, 11.1))
plt.ylim((-0.1, 1.1))

if model == 0:
	plt.title(r'Barabasi Albert Model w/ $<k> = 4$')
elif model == 1:
	plt.title(r'DMS Minimal Model w/ $<k> = 4$')
elif model == 2:
	plt.title(r'Power Law Model w/ $<k> = 2$')
elif model == 3:
	plt.title(r'Power Law Model w/ $<k> = 4$')
elif model == 4:
	plt.title(r'Random Graph Model w/ $<k> = 4$')
elif model == 5:
	plt.title(r'Watts-Strogatz Model w/ $<k> = 4$')
elif model == 6:
	plt.title(r'Power Grid Network')
else:
	plt.title(r'Internet Network')

plt.grid()
plt.legend()
plt.xlabel(r'\textbf{$\alpha$}', fontsize=11)
plt.ylabel(r'\textbf{Fraction of unconnected pairs of nodes}', fontsize=11)

plt.show()

fig_name = "Plots/figures/unc_pairs_nodes_%i.png" % model

f1.savefig(fig_name, bbox_inches='tight')
