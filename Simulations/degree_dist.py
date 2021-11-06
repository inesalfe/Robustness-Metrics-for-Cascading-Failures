import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def degree_dist():
    graphs = {0: 'ba', 1: 'dms', 2: 'pl2', 3: 'pl4', 4: 'rand', 5: 'ws', 6: 'power', 7: 'as-22july06'}
    graphs_name = {0: r'Barabási-Albert', 1: r'DMS', 
                   2: r'Powerlaw w/ $\langle k\rangle=2$', 3: r'Powerlaw w/ $\langle k\rangle=4$', 
                   4: r'Random Erdos-Rényi', 5: r'Watts-Strogatz', 
                   6: r'Power Grid', 7: r'Internet'}
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
            if model >=0 or model <=7:
                break    
        except ValueError:
            print("Please an integer between 0 and 7:")

    deg_max = 21 if model == 6 else 10 if model == 5 else 16 if model == 4 else 100
    
    degree_freq = [0 for _ in range(deg_max)]
    cummulative_vcount = 0
    its = 1 if model in (6,7) else 10
    for i in range(its):
        filename = "Simulations/Graphs/%s" % graphs[model]
        if its != 1:
            filename += '_%d' % i
        filename += '.gml'
        G = nx.read_gml(filename, None)

        for _, deg in G.degree():
            if(deg < deg_max):
                degree_freq[deg] += 1
        cummulative_vcount += G.number_of_nodes()

    degree_freq = np.divide(degree_freq, cummulative_vcount)

    for i in range(deg_max - 2, -1, -1):
        degree_freq[i] += degree_freq[i + 1]

    # plt.rc('text', usetex=True)
    # plt.rc('font', family='serif')

    plot = plt.plot if model in (4, 5) else (plt.semilogy if model == 6 else plt.loglog)
    
    f1 = plt.figure()
    plot(range(deg_max), degree_freq, 'o-')
    plt.ylabel(r'Average Cummulative Degree Distibution $P_{avg}(k)$', fontsize=15)
    plt.xlabel(r'Degree, $k$', fontsize=15)
    plt.title(rf'{graphs_name[model]} Network Degree Distribution', fontsize=18)
    if model not in (4, 5, 6):
        plot([k+2 for k in range(deg_max)], [4*(k + 2)**(-2) for k in range(deg_max)], 'g--', label=r'$P(k) \sim k^{-\gamma + 1}, \ \gamma = 3$')
        plt.legend(fontsize=14)
    # plt.xlim(0, np.max([i for i, f in enumerate(degree_freq) if f != 0]) + 5)
    plt.grid()
    plt.show()

    fig_name = "Plots/figures/degree_dist_%i.png" % model
    f1.savefig(fig_name, bbox_inches='tight')


if __name__ == '__main__':
    degree_dist()
