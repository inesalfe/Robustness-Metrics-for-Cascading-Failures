#include <igraph.h>
#include <iostream>

using namespace std;

int main() {

	// Path to the output file
	char file_name[27] = "Animation/Graphs/small.gml";

	FILE * file;

	file = fopen(file_name, "w");
	if (file == 0) {
		exit(1);
	}

	igraph_t graph; // The graph itself
	igraph_vector_t v; // Auxiliary vector for the edges

	// Edges vector where each pair of numbers represents one edge
	igraph_real_t edges[] = {0, 1, 1, 2, 2, 3, 2, 5, 3, 5, 3, 4, 4, 5, 5, 6, 6, 7, 6, 8, 6, 9, 7, 8, 8, 9, 9, 10, 8, 10, 2, 9, 4, 7};
	
	igraph_vector_view(&v, edges, sizeof(edges) / sizeof(double));
	igraph_create(&graph, &v, 0, IGRAPH_UNDIRECTED); // Creation of an undirected graph

	igraph_write_graph_gml(&graph, file, NULL, 0);
	
	fclose(file);

	igraph_destroy(&graph);

	return 0;

}