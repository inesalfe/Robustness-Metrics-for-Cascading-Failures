#include <igraph.h>
#include <iostream>

using namespace std;

int main() {

	int N;

	igraph_t graph; // The graph itself
	igraph_vector_t clusters;
	igraph_vector_t comp; // Size of the components
	igraph_vector_t deleted_nodes; // Size of the components

	igraph_vector_init(&clusters, 0);
	igraph_vector_init(&comp, 0);
	igraph_vector_init(&deleted_nodes, 0);

	// Path to the output file
	char file_name[40] = "Simulations/Graphs/rand_0.gml";

	int file_counter = 0;

	igraph_rng_seed(igraph_rng_default(), 0);

	N = 5120;

	while(file_counter < 10) {

		igraph_erdos_renyi_game(&graph, IGRAPH_ERDOS_RENYI_GNM, N, 1.96*N, IGRAPH_UNDIRECTED, IGRAPH_NO_LOOPS);

		FILE * file;

		// Change path name according to the network
		file_name[24] = file_counter + '0';

		file = fopen(file_name, "w");
		if (file == 0) {
			exit(1);
		}
			
		igraph_integer_t n_comp;

		igraph_clusters(&graph, &clusters, &comp, &n_comp, IGRAPH_WEAK);

		long L_comp = igraph_vector_which_max(&comp);
		long L_comp_size = igraph_vector_max(&comp);

		for (int i = 0; i < N; i++) {
			if (VECTOR(clusters)[i] != L_comp)
				igraph_vector_push_back(&deleted_nodes, i);
		}

		igraph_vs_t v_del;

		igraph_vs_vector(&v_del, &deleted_nodes);
		igraph_delete_vertices(&graph, v_del);

		igraph_clusters(&graph, &clusters, &comp, &n_comp, IGRAPH_WEAK);

		L_comp = igraph_vector_which_max(&comp);
		L_comp_size = igraph_vector_max(&comp);

		double avgd = 2.0 * igraph_ecount(&graph) / igraph_vcount(&graph);

		cout << "Number of nodes: " << igraph_vcount(&graph) << endl;
		cout << "Number of components: " << n_comp << endl;
		cout << "Size of the largest component: " << L_comp_size << endl;
		cout << "Largest component id: " << L_comp << endl;
		cout << "Average degree: " << avgd << endl;

		if (avgd > 3.985 && avgd < 4.015 && igraph_vcount(&graph) > 4950 && igraph_vcount(&graph) < 5050) {
			cout << "WRITTEN" << endl;
			igraph_write_graph_gml(&graph, file, NULL, 0);
			file_counter++;
		}
		
		fclose(file);

		igraph_vector_clear(&clusters);
		igraph_vector_clear(&deleted_nodes);
		igraph_vector_clear(&comp);

		igraph_destroy(&graph);

	}

	igraph_vector_destroy(&clusters);
	igraph_vector_destroy(&comp);

	return 0;

}