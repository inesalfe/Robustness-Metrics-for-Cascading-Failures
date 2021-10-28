#include <igraph.h>
#include <iostream>

using namespace std;

#define N 500 // Number of nodes
#define M 2 // New edges per iteration

int main() {

	igraph_t graph; // The graph itself

	// Path to the output file
	char file_name[24] = "Animation/Graphs/ba.gml";

	FILE * file;

	file = fopen(file_name, "w");
	if (file == 0) {
		exit(1);
	}

	// Create graph using the barabasi albert model
	igraph_rng_seed(igraph_rng_default(), 0);
	igraph_barabasi_game(&graph, N, 1, M, NULL, true, 1, false, IGRAPH_BARABASI_BAG, 0); 

	igraph_write_graph_gml(&graph, file, NULL, 0);
	
	fclose(file);

	igraph_destroy(&graph);

	return 0;

}