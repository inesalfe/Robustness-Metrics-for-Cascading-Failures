import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

model = 0
while True:
	try:
		model = int(input("Choose model (0 - BA; 1 - DMS; 2 - PL; 3 - BA w/ M=1): "))       
	except ValueError:
		print("Please enter 0, 1, 2 or 3:")
		continue
	else:
		if model == 0 or model == 1 or model == 2 or model == 3:
			break
		else:
			continue

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

if model == 0:
	folder = "Data/BA/"
elif model == 1:
	folder = "Data/DMS/"
elif model == 2:
	folder = "Data/PL/"
else:
	folder = "Data/BA_M1/"

file_name = "data_%i.txt" % criteria

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

f1 = plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = list(range(1, len(avg_del[2])+1))

plt.plot(x, avg_del[2], color="blue", label="Average", marker='o')

plt.fill_between(x, avg_del[2]-std_del[2], avg_del[2]+std_del[2], color="red", alpha=0.1, label='Standard Deviation')

plt.fill_between(x, min_del[2], max_del[2], color="blue", alpha=0.1, label='Maximum and Minimum')

if model == 0:
	plt.title('Barabási Albert Model')
elif model == 1:
	plt.title('DMS Minimal Model')
elif model == 2:
	plt.title('Power Law Model')
else:
	plt.title('Barabási Albert Model w/ M = 1')

plt.yscale('log')
plt.grid()
plt.legend()
plt.xlabel(r'Time Stamp', fontsize=11)
plt.ylabel(r'\# Deleted Nodes', fontsize=11)

plt.show()

file_name = "Plots/figures/v_del_%i.png" % criteria

f1.savefig(file_name, bbox_inches='tight')