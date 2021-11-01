import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

model = 0
while True:
	try:
		model = int(input("Choose model (0 - BA; 1 - DMS; 2 - PL2; 3 - PL4; 4 - RAND; 5 - WS): "))       
	except ValueError:
		print("Please enter 0, 1, 2, 3, 4 ou 5:")
		continue
	else:
		if model == 0 or model == 1 or model == 2 or model == 3 or model == 4 or model == 5:
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
else:
	folder = "Data/WS/"

file_name = "data_2.txt"

with open(folder + file_name) as f:
	lines = f.read().splitlines()

if model == 2:
	N = [int(i) for i in lines[0].split()[1:]]
else:
	N = [int(lines[0].split()[1]) for i in range(10)]

N_GRAPHS = int(lines[1].split()[1])
IT = int(lines[2].split()[1])
alphas = lines[4].split()[1:12]

deleted_v = [[] for _ in range(len(alphas))]
max_del = [[] for _ in range(len(alphas))]
min_del = [[] for _ in range(len(alphas))]
avg_del = [[] for _ in range(len(alphas))]
var_del = [[] for _ in range(len(alphas))]
std_del = [[] for _ in range(len(alphas))]

l_it = 0
for net in range(N_GRAPHS):
	for a in range(len(alphas)):
		for it in range(IT):
			deleted_v[a].append(lines[5+6*l_it].split()[1:])
			l_it += 1

for a in range(len(alphas)):
	max_len = np.max([len(v) for v in deleted_v[a]])
	for l in deleted_v[a]:
		l.extend([0]*(max_len-len(l)))
	for it in range(1, max_len):
		avg = int(np.mean([int(v[it]) for v in deleted_v[a]]))
		if (avg == 0):
			break
		max_del[a].append(np.max([int(v[it]) for v in deleted_v[a]]))
		min_del[a].append(np.min([int(v[it]) for v in deleted_v[a]]))
		avg_del[a].append(avg)
		var_del[a].append(np.var([int(v[it]) for v in deleted_v[a]]))
		std_del[a] = np.sqrt(var_del[a])

curr_alpha = 2

f1 = plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = list(range(1, len(avg_del[curr_alpha])+1))

plt.plot(x, avg_del[curr_alpha], color="blue", label="Average", marker='o')

plt.fill_between(x, avg_del[curr_alpha]-std_del[curr_alpha], avg_del[curr_alpha]+std_del[curr_alpha], color="red", alpha=0.1, label='Standard Deviation')

plt.fill_between(x, min_del[curr_alpha], max_del[curr_alpha], color="blue", alpha=0.1, label='Maximum and Minimum')

if model == 0:
	plt.title(r'Barabási Albert Model $\rightarrow \alpha=0.7$')
elif model == 1:
	plt.title(r'DMS Minimal Model $\rightarrow \alpha=0.7$')
elif model == 2:
	plt.title(r'Power Law Model w/ $<k> = 2 \rightarrow \alpha=0.7$')
elif model == 3:
	plt.title(r'Power Law Model w/ $<k> = 4 \rightarrow \alpha=0.7$')
elif model == 4:
	plt.title(r'Random Graph Model w/ $<k> = 4 \rightarrow \alpha=0.7$')
else:
	plt.title(r'Watts-Strogatz Model $\rightarrow \alpha=0.7$')

plt.yscale('log')
plt.grid()
plt.legend()
plt.xlabel(r'Time Stamp', fontsize=11)
plt.ylabel(r'\# Deleted Nodes', fontsize=11)

plt.show()

file_name = "Plots/figures/v_del_%i_02.png" % model

f1.savefig(file_name, bbox_inches='tight')

curr_alpha = 5

f2 = plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = list(range(1, len(avg_del[curr_alpha])+1))

plt.plot(x, avg_del[curr_alpha], color="blue", label="Average", marker='o')

plt.fill_between(x, avg_del[curr_alpha]-std_del[curr_alpha], avg_del[curr_alpha]+std_del[curr_alpha], color="red", alpha=0.1, label='Standard Deviation')

plt.fill_between(x, min_del[curr_alpha], max_del[curr_alpha], color="blue", alpha=0.1, label='Maximum and Minimum')

if model == 0:
	plt.title(r'Barabási Albert Model $\rightarrow \alpha=0.7$')
elif model == 1:
	plt.title(r'DMS Minimal Model $\rightarrow \alpha=0.7$')
elif model == 2:
	plt.title(r'Power Law Model w/ $<k> = 2 \rightarrow \alpha=0.7$')
elif model == 3:
	plt.title(r'Power Law Model w/ $<k> = 4 \rightarrow \alpha=0.7$')
elif model == 4:
	plt.title(r'Random Graph Model w/ $<k> = 4 \rightarrow \alpha=0.7$')
else:
	plt.title(r'Watts-Strogatz Model $\rightarrow \alpha=0.7$')

plt.yscale('log')
plt.grid()
plt.legend()
plt.xlabel(r'Time Stamp', fontsize=11)
plt.ylabel(r'\# Deleted Nodes', fontsize=11)

plt.show()

file_name = "Plots/figures/v_del_%i_05.png" % model

f2.savefig(file_name, bbox_inches='tight')

curr_alpha = 7

f3 = plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = list(range(1, len(avg_del[curr_alpha])+1))

plt.plot(x, avg_del[curr_alpha], color="blue", label="Average", marker='o')

plt.fill_between(x, avg_del[curr_alpha]-std_del[curr_alpha], avg_del[curr_alpha]+std_del[curr_alpha], color="red", alpha=0.1, label='Standard Deviation')

plt.fill_between(x, min_del[curr_alpha], max_del[curr_alpha], color="blue", alpha=0.1, label='Maximum and Minimum')

if model == 0:
	plt.title(r'Barabási Albert Model $\rightarrow \alpha=0.7$')
elif model == 1:
	plt.title(r'DMS Minimal Model $\rightarrow \alpha=0.7$')
elif model == 2:
	plt.title(r'Power Law Model w/ $<k> = 2 \rightarrow \alpha=0.7$')
elif model == 3:
	plt.title(r'Power Law Model w/ $<k> = 4 \rightarrow \alpha=0.7$')
elif model == 4:
	plt.title(r'Random Graph Model w/ $<k> = 4 \rightarrow \alpha=0.7$')
else:
	plt.title(r'Watts-Strogatz Model $\rightarrow \alpha=0.7$')

plt.yscale('log')
plt.grid()
plt.legend()
plt.xlabel(r'Time Stamp', fontsize=11)
plt.ylabel(r'\# Deleted Nodes', fontsize=11)

plt.show()

file_name = "Plots/figures/v_del_%i_07.png" % model

f3.savefig(file_name, bbox_inches='tight')