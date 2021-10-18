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
big_del = [[] for _ in range(len(alphas))]
small_del = [[] for _ in range(len(alphas))]
avg_del = [[] for _ in range(len(alphas))]

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
	for it in range(max_len):
		big_del[a].append(np.max([int(v[it]) for v in deleted_v[a]]))
		small_del[a].append(np.min([int(v[it]) for v in deleted_v[a]]))
		avg_del[a].append(int(np.mean([int(v[it]) for v in deleted_v[a]])))

f1 = plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = list(range(1, len(avg_del[2])+1))

plt.plot(x, avg_del[2], color="blue", label="?")

er_inferior = [x1 - x2 for (x1, x2) in zip(avg_del[2], small_del[2])]
er_superior = [x1 - x2 for (x1, x2) in zip(big_del[2], avg_del[2])]

error = np.array([er_inferior, er_superior])
np.resize(error,(2,len(small_del[2])))
plt.errorbar(x, avg_del[2], yerr=error, fmt='bo', markersize=5, capsize=5, ecolor="black")

plt.yscale('log')
plt.grid()
plt.legend()
plt.xlabel(r'Time Stamp', fontsize=11)
plt.ylabel(r'\# Deleted Nodes', fontsize=11)
# plt.xlim((-1.1, 11.1))
# plt.ylim((-0.1, 1.1))

plt.show()

f1.savefig("v_del.png", bbox_inches='tight')