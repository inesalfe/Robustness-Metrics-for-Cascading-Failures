#include <igraph.h>
#include <iostream>

using namespace std;

#define N 5000 // Number of nodes
#define N_GRAPHS 10 // Number of repetitions

int main() {

	igraph_t graph; // The graph itself

	// Path to the output file
	char file_name[35] = "Simulations/Graphs/rand_0.gml";

	igraph_rng_seed(igraph_rng_default(), 0);

	for(int n = 0; n < N_GRAPHS; ++n) {

		FILE * file;

		// Change path name according to the network
		file_name[24] = n + '0';

		file = fopen(file_name, "w");
		if (file == 0) {
			exit(1);
		}

		// Create graph using the barabasi albert model
		igraph_erdos_renyi_game(&graph, IGRAPH_ERDOS_RENYI_GNP, N, 4/(N-1), false, false);		// std::cout << "Nodes: " << igraph_vcount(&graph) << " Edges: " << igraph_ecount(&graph) << std::endl;
		igraph_write_graph_gml(&graph, file, NULL, 0);
		
		fclose(file);

		igraph_destroy(&graph);

	}

	return 0;

}