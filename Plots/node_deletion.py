import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

criteria = 0
while True:
	try:
		criteria = int(input("Choose criteria (0, 1, 2 or 3): "))       
	except ValueError:
		print("Please enter an integer between 0 and 3:")
		continue
	else:
		if criteria >= 0 and criteria <= 3:
			break
		else:
			continue

file_name = "../Data/data_%i.txt" % criteria

with open(file_name) as f:
	lines = f.read().splitlines()

N = int(lines[0].split()[1])
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
			deleted_v[a].append(lines[5+5*l_it].split()[1:])
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

f1 = plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = list(range(1, len(avg_del[2])+1))

plt.plot(x, avg_del[2], color="blue", label="Average", marker='o')

plt.fill_between(x, avg_del[2]-std_del[2], avg_del[2]+std_del[2], color="red", alpha=0.1, label='Standard Deviation')

plt.fill_between(x, min_del[2], max_del[2], color="blue", alpha=0.1, label='Maximum and Minimum')

plt.yscale('log')
plt.grid()
plt.legend()
plt.xlabel(r'Time Stamp', fontsize=11)
plt.ylabel(r'\# Deleted Nodes', fontsize=11)

plt.show()

file_name = "v_del_%i.png" % criteria

f1.savefig(file_name, bbox_inches='tight')