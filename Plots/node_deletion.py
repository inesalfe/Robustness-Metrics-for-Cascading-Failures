import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import math

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
		7 - Internet Network.\n>>> """))       
	except ValueError:
		print("Please an integer between 0 and 7:")
		continue
	else:
		if model >=0 and model <=7:
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

file_name = "data_2.txt"

with open(folder + file_name) as f:
	lines = f.read().splitlines()

if model == 2 or model == 3 or model == 4:
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

plt.fill_between(x, avg_del[curr_alpha]-std_del[curr_alpha], avg_del[curr_alpha]+std_del[curr_alpha], color="blue", alpha=0.1, label='Standard Deviation')

# plt.fill_between(x, min_del[curr_alpha], max_del[curr_alpha], color="blue", alpha=0.1, label='Maximum and Minimum')

if model == 0:
	plt.title(r'Barabási Albert Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.2$', fontsize=18)
elif model == 1:
	plt.title(r'DMS Minimal Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.2$', fontsize=18)
elif model == 2:
	plt.title(r'Power Law Model w/ $\langle k \rangle \approx 2 \rightarrow \alpha=0.2$', fontsize=18)
elif model == 3:
	plt.title(r'Power Law Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.2$', fontsize=18)
elif model == 4:
	plt.title(r'Random Graph Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.2$', fontsize=18)
elif model == 5:
	plt.title(r'Watts-Strogatz Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.2$', fontsize=18)
elif model == 6:
	plt.title(r'Power Grid Network $\rightarrow \alpha=0.2$', fontsize=18)
else:
	plt.title(r'Internet Network $\rightarrow \alpha=0.2$', fontsize=18)

xint = range(min(x), math.ceil(max(x))+1)
plt.xticks(xint)

plt.yscale('log')
plt.grid()
if model != 6:
	plt.legend(fontsize=14)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel(r'Time Stamp', fontsize=15)
plt.ylabel(r'\# Deleted Nodes', fontsize=15)

plt.show()

file_name = "Plots/figures/v_del_%i_02.png" % model

f1.savefig(file_name, bbox_inches='tight')

curr_alpha = 5

f2 = plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = list(range(1, len(avg_del[curr_alpha])+1))

plt.plot(x, avg_del[curr_alpha], color="blue", label="Average", marker='o')

plt.fill_between(x, avg_del[curr_alpha]-std_del[curr_alpha], avg_del[curr_alpha]+std_del[curr_alpha], color="blue", alpha=0.1, label='Standard Deviation')

# plt.fill_between(x, min_del[curr_alpha], max_del[curr_alpha], color="blue", alpha=0.1, label='Maximum and Minimum')

if model == 0:
	plt.title(r'Barabási Albert Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.5$', fontsize=18)
elif model == 1:
	plt.title(r'DMS Minimal Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.5$', fontsize=18)
elif model == 2:
	plt.title(r'Power Law Model w/ $\langle k \rangle \approx 2 \rightarrow \alpha=0.5$', fontsize=18)
elif model == 3:
	plt.title(r'Power Law Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.5$', fontsize=18)
elif model == 4:
	plt.title(r'Random Graph Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.5$', fontsize=18)
elif model == 5:
	plt.title(r'Watts-Strogatz Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.5$', fontsize=18)
elif model == 6:
	plt.title(r'Power Grid Network $\rightarrow \alpha=0.5$', fontsize=18)
else:
	plt.title(r'Internet Network $\rightarrow \alpha=0.5$', fontsize=18)

xint = range(min(x), math.ceil(max(x))+1)
plt.xticks(xint)

plt.yscale('log')
plt.grid()
if model != 6:
	plt.legend(fontsize=14)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel(r'Time Stamp', fontsize=15)
plt.ylabel(r'\# Deleted Nodes', fontsize=15)

plt.show()

file_name = "Plots/figures/v_del_%i_05.png" % model

f2.savefig(file_name, bbox_inches='tight')

curr_alpha = 7

f3 = plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = list(range(1, len(avg_del[curr_alpha])+1))

plt.plot(x, avg_del[curr_alpha], color="blue", label="Average", marker='o')

plt.fill_between(x, avg_del[curr_alpha]-std_del[curr_alpha], avg_del[curr_alpha]+std_del[curr_alpha], color="blue", alpha=0.1, label='Standard Deviation')

# plt.fill_between(x, min_del[curr_alpha], max_del[curr_alpha], color="blue", alpha=0.1, label='Maximum and Minimum')

if model == 0:
	plt.title(r'Barabási Albert Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.7$', fontsize=18)
elif model == 1:
	plt.title(r'DMS Minimal Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.7$', fontsize=18)
elif model == 2:
	plt.title(r'Power Law Model w/ $\langle k \rangle \approx 2 \rightarrow \alpha=0.7$', fontsize=18)
elif model == 3:
	plt.title(r'Power Law Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.7$', fontsize=18)
elif model == 4:
	plt.title(r'Random Graph Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.7$', fontsize=18)
elif model == 5:
	plt.title(r'Watts-Strogatz Model w/ $\langle k \rangle \approx 4 \rightarrow \alpha=0.7$', fontsize=18)
elif model == 6:
	plt.title(r'Power Grid Network $\rightarrow \alpha=0.7$', fontsize=18)
else:
	plt.title(r'Internet Network $\rightarrow \alpha=0.7$', fontsize=18)

xint = range(min(x), math.ceil(max(x))+1)
plt.xticks(xint)

plt.yscale('log')
plt.grid()
if model != 6:
	plt.legend(fontsize=14)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel(r'Time Stamp', fontsize=15)
plt.ylabel(r'\# Deleted Nodes', fontsize=15)

plt.show()

file_name = "Plots/figures/v_del_%i_07.png" % model

f3.savefig(file_name, bbox_inches='tight')