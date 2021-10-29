#include <igraph.h>
#include <time.h>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

#define N 5000 // Number of nodes
#define N_GRAPHS 10 // Number of repetitions
#define M 2 // New edges per iteration
// Average degre is 2 * M
#define IT 5 // Iteration of the same network per alpha

void print_vector(igraph_vector_t *v) {
	long int i, l = igraph_vector_size(v);
	for (i = 0; i < l; i++)
		printf("%li ", (long int) VECTOR(*v)[i]);
	printf("\n");
}

int main() {

	int criteria = 4;

	ofstream output_file;
	output_file.open("../Data/data_4.txt");

	igraph_t graph, graph_cp; // The graph itself
	igraph_vector_t v; // Auxiliary vector for the edges
	igraph_vector_t deletion_list; 	// List with the vertices to delete - updated in each iteration
	igraph_vector_t del_edges; // Edges to be deleted in each iteration 
	igraph_vector_ptr_t short_paths; // Auxiliary vector for the shorthest paths
	igraph_vector_t comp; // Size of the components
	igraph_vector_t capacity; // The capacity of each vertex equals the initial betweeness centrality
	igraph_vector_t capacity_cp; // The capacity of each vertex equals the initial betweeness centrality
	igraph_vector_t capacity_sorted; // Sorted capacity
	igraph_vector_t curr_bc; // Betweeness centrality in a given moment
	igraph_es_t del_edges_sel; // Edges to be deleted in each iteration in selector mode

	output_file << "N " << N << endl;
	output_file << "N_NET " << N_GRAPHS << endl;
	output_file << "IT " << IT << endl;
	output_file << "CRITERIA " << criteria << endl;
	output_file << "ALPHAS ";

	vector<double> alphas(11);
	vector<vector<double>> ratios(11, vector<double>(10,0));
	for(int i = 0; i < 11; ++i) {
		alphas[i] = .1 * i;
		output_file << " " << alphas[i];
	}

	output_file << endl;

	igraph_rng_seed(igraph_rng_default(), time(NULL));
	igraph_vector_init(&comp, 0);
	igraph_vector_init(&capacity, N);
	igraph_vector_init(&curr_bc, N);
	igraph_vector_init(&deletion_list, 0);
	igraph_vector_init(&del_edges, 0);
	igraph_vector_init(&capacity_sorted, 0);

	vector<long> initial_edges;

	for(int n = 0; n < N_GRAPHS; ++n) {

		cout << "#################### NETWORK Nº " << n + 1 << " ####################" << endl;
		/* GRAPH TYPE CHOICE */
		igraph_barabasi_game(&graph, N, 1, M, NULL, true, 1, false, IGRAPH_BARABASI_BAG, 0); 

		/* GRAPH INITIAL INFORMATION */
		cout << "Number of Nodes: " << N << endl;
		cout << "Average Degree: " << (2.0 * igraph_ecount(&graph) / igraph_vcount(&graph)) << endl;

		/* CAPACITY METRIC */
		// Betweeness centrality
		igraph_edge_betweenness(&graph, &capacity, false, NULL);

		/* CHOOSE INITIAL VERTEX TO DELETE... */
		long initial_edge;
		// ... HIGHEST LOAD
		igraph_vector_copy(&capacity_sorted, &capacity);
		igraph_vector_reverse_sort(&capacity_sorted);
		for (int i = 0; i < IT; i++) {
			igraph_vector_search(&capacity, 0, VECTOR(capacity_sorted)[i], &initial_edge);
			initial_edges.push_back(initial_edge);
		}

		/* FOR EACH NETWORK RUM FOR EACH ALPHA */
		for(int a = 0; a < 11; ++a) {
			cout << "########## ALPHA = " << alphas[a] <<  " ##########" << endl;
			igraph_vector_copy(&capacity_cp, &capacity);
			/* SCALE CAPACITY BY alpha */
			igraph_vector_scale(&capacity_cp, (igraph_real_t) (1 + alphas[a]));

			for(int it = 0; it < IT; ++it) {

				cout << endl << "##### Iteration " << it + 1 << "/" << IT << " #####" << endl;
				igraph_copy(&graph_cp, &graph);

				igraph_vector_push_back(&deletion_list, initial_edges[it]);

				cout << "Initial Node: " << initial_edges[it] << endl << "Initial Edge Capacity: " << VECTOR(capacity_cp)[initial_edges[it]] << endl;

				output_file << "N_E_TO_DELETE";

				/* MAIN LOOP */
				int iterations = 0;
				while(!igraph_vector_empty(&deletion_list)) {

					output_file << " " << igraph_vector_size(&deletion_list);

					++iterations;

					// Delete edges in the deletion list
					igraph_es_vector(&del_edges_sel, &deletion_list);
					igraph_delete_edges(&graph_cp, del_edges_sel);
					igraph_vector_clear(&deletion_list);

					// Recalculate the betweeness centralities
					igraph_edge_betweenness(&graph_cp, &curr_bc, false, NULL);

					// Create new deletion_list
					for(int i = 0; i < igraph_vector_size(&curr_bc); ++i) {
						if (VECTOR(curr_bc)[i] > VECTOR(capacity_cp)[i]) {
							igraph_vector_push_back(&deletion_list, i);
						}
					}
				}

				// PRINT THE TOTAL NUMBER OF CASCADING ITERATIONS
				cout << endl << "Iterations: " << iterations << endl << endl;
				
				output_file << endl << "ITER " << iterations << endl;

				/* GRAPH FINAL INFORMATION */
				int n_comp;
				igraph_clusters(&graph_cp, NULL, &comp, &n_comp, IGRAPH_WEAK);
				long final_L_comp = igraph_vector_max(&comp);
				cout << "Final Number of Components: " << n_comp << "\nLargest component: " << final_L_comp << endl;
				cout << "Final Average Degree: " << (2.0 * igraph_ecount(&graph_cp) / igraph_vcount(&graph_cp)) << endl;
				
				output_file << "N_COMP " << n_comp << endl;
				output_file << "L_COMP " << final_L_comp << endl;
				output_file << "D_FINAL " << (2.0 * igraph_ecount(&graph_cp) / igraph_vcount(&graph_cp)) << endl;

				igraph_destroy(&graph_cp);
			
			}
			igraph_vector_destroy(&capacity_cp);

		}
		igraph_destroy(&graph);
		initial_edges.clear();

	}

	output_file.close();

	// Free memory
	igraph_vector_destroy(&capacity);
	igraph_vector_destroy(&deletion_list);
	igraph_vector_destroy(&del_edges);
	igraph_vector_destroy(&curr_bc);
	igraph_vector_destroy(&comp);
	igraph_vector_destroy(&capacity_sorted);

	return 0;

}