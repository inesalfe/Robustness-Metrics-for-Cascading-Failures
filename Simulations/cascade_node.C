#include <igraph.h>
#include <time.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <string.h>

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

	cout << "Please choose the model:" << endl;
	cout << "0 - Barabasi Albert" << endl;
	cout << "1 - DMS Minimal Model" << endl;

	int model;
	cin >> model;
	while(cin.fail() || model < 0 || model > 1) {
		cout << "Invalid Input" << endl;
		cin.clear();
		cin.ignore(256,'\n');
		cin >> model;
	}

	cout << "Please choose the criteria for node eliminatiton:" << endl;
	cout << "0 - RANDOM" << endl;
	cout << "1 - HIGHEST LOAD (BETWEENNESS CENTRALITY)" << endl;
	cout << "2 - HIGHEST AVERAGE DEGREE" << endl;
	cout << "3 - HIGHEST CLUSTERING COEFICIENT" << endl;

	int criteria;
	cin >> criteria;
	while(cin.fail() || criteria < 0 || criteria > 3) {
		cout << "Invalid Input" << endl;
		cin.clear();
		cin.ignore(256,'\n');
		cin >> criteria;
	}

	char file_name[50] = {0};
	if (model == 0)
		strcpy(file_name, "Data/BA/data.txt");
	else
		strcpy(file_name, "Data/DMS/data.txt");

	FILE *output_file = fopen(file_name, "w");
	if (output_file == 0) {
		cout << "Unable to open output file " << file_name << ". Exiting\n";
		return 10;
	}

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
	igraph_vector_t degree_sorted; // Sorted degree of each vertex
	igraph_vector_t clustering_sorted; // Sorted clustering coeficient of each vertex
	igraph_vector_t degree; // Degree of each vertex
	igraph_vector_t clustering; // Clustering coeficient of each vertex
	igraph_matrix_t m; // Matrix to hold the shortest path between each pair of nodes
	igraph_vector_t deleted_nodes; 	// List with the deleted nodes in each iteration

	fprintf(output_file, "N %d\n", N);
	fprintf(output_file, "N_NET %d\n", N_GRAPHS);
	fprintf(output_file, "IT %d\n", IT);
	fprintf(output_file, "CRITERIA %d\n", criteria);
	fprintf(output_file, "ALPHAS");

	vector<double> alphas(11);
	vector<vector<double>> ratios(11, vector<double>(10,0));
	for(int i = 0; i < 11; ++i) {
		alphas[i] = .1 * i;
		fprintf(output_file, " %.1f", alphas[i]);
	}

	fprintf(output_file, "\n");

	igraph_rng_seed(igraph_rng_default(), 0);
	igraph_vector_init(&comp, 0);
	igraph_vector_init(&capacity, N);
	igraph_vector_init(&curr_bc, N);
	igraph_vector_init(&deletion_list, 0);
	igraph_vector_init(&del_edges, 0);
	igraph_vector_init(&capacity_sorted, 0);
	igraph_vector_init(&degree_sorted, 0);
	igraph_vector_init(&clustering_sorted, 0);
	igraph_vector_init(&degree, N);
	igraph_vector_init(&clustering, N);
	igraph_vector_init(&deleted_nodes, 0);
	igraph_matrix_init(&m, 0, 0);

	vector<long> initial_nodes;

	for(int n = 0; n < N_GRAPHS; ++n) {

		cout << "#################### NETWORK Nº " << n + 1 << " ####################" << endl;
		/* GRAPH TYPE CHOICE */

		if (model == 0)
			igraph_barabasi_game(&graph, N, 1, M, NULL, true, 1, false, IGRAPH_BARABASI_BAG, 0); 
		else {
			char filename[50] = {0};
			sprintf(filename, "Simulations/graphs/dms_%d.gml", n);

			FILE *input_file = fopen(filename, "r");
			if (input_file == 0) {
				cout << "Unable to open input file " << filename << ". Exiting\n";
				return 11;
			}

			igraph_read_graph_gml(&graph, input_file);
			fclose(input_file);

		}

		/* GRAPH INITIAL INFORMATION */
		cout << "Number of Nodes: " << N << endl;
		cout << "Average Degree: " << (2.0 * igraph_ecount(&graph) / igraph_vcount(&graph)) << endl;

		/* CAPACITY METRIC */
		// Betweeness centrality
		igraph_betweenness(&graph, &capacity, igraph_vss_all(), IGRAPH_UNDIRECTED, NULL);

		/* CHOOSE INITIAL VERTEX TO DELETE... */
		long initial_node;
		switch (criteria) {
			case 0:
				// ... RANDOMLY
				srandom(time(NULL));
				for (int i = 0; i < IT; i++) {
					initial_nodes.push_back(random() % N);
				}
				break;
			case 1:
				// ... HIGHEST LOAD
				igraph_vector_copy(&capacity_sorted, &capacity);
				igraph_vector_reverse_sort(&capacity_sorted);
				for (int i = 0; i < IT; i++) {
					igraph_vector_search(&capacity, 0, VECTOR(capacity_sorted)[i], &initial_node);
					initial_nodes.push_back(initial_node);
				}
				break;
			case 2:
				// ... HIGHEST AVERAGE DEGREE
				igraph_degree(&graph, &degree, igraph_vss_all(), IGRAPH_ALL, false);
				igraph_vector_copy(&degree_sorted, &degree);
				igraph_vector_reverse_sort(&degree_sorted);
				for (int i = 0; i < IT; i++) {
					igraph_vector_search(&degree, 0, VECTOR(degree_sorted)[i], &initial_node);
					initial_nodes.push_back(initial_node);
				}
				break;
			case 3:
				// ... HIGHEST CLUSTERING COEFICIENT
				igraph_transitivity_local_undirected(&graph, &clustering, igraph_vss_all(), IGRAPH_TRANSITIVITY_ZERO);
				igraph_vector_copy(&clustering_sorted, &clustering);
				igraph_vector_reverse_sort(&clustering_sorted);
				for (int i = 0; i < IT; i++) {
					igraph_vector_search(&clustering, 0, VECTOR(clustering_sorted)[i], &initial_node);
					initial_nodes.push_back(initial_node);
				}
				break;
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

				igraph_vector_push_back(&deletion_list, initial_nodes[it]);

				cout << "Initial Node: " << initial_nodes[it] << endl << "Initial Node Capacity: " << VECTOR(capacity_cp)[initial_nodes[it]] << endl;

				fprintf(output_file, "N_V_TO_DELETE");

				/* MAIN LOOP */
				int iterations = 0;
				while(!igraph_vector_empty(&deletion_list)) {

					fprintf(output_file, " %ld", igraph_vector_size(&deletion_list));

					++iterations;

					// Delete edges incident in the vertices in the deletion list
					while(!igraph_vector_empty(&deletion_list)) {
						igraph_vector_push_back(&deleted_nodes, igraph_vector_tail(&deletion_list));
						igraph_incident(&graph_cp, &del_edges, igraph_vector_pop_back(&deletion_list), IGRAPH_ALL);
						igraph_es_vector(&del_edges_sel, &del_edges);
						igraph_delete_edges(&graph_cp, del_edges_sel);
					}

					// Recalculate the betweeness centralities
					igraph_betweenness(&graph_cp, &curr_bc, igraph_vss_all(), IGRAPH_UNDIRECTED, NULL);
					
					// Create new deletion_list
					for(int i = 0; i < igraph_vector_size(&curr_bc); ++i) {
						if (VECTOR(curr_bc)[i] > VECTOR(capacity_cp)[i]) {
							igraph_vector_push_back(&deletion_list, i);
						}
					}
				}

				// PRINT THE TOTAL NUMBER OF CASCADING ITERATIONS
				cout << endl << "Iterations: " << iterations << endl << endl;
				
				fprintf(output_file, "\nITER %d", iterations);

				igraph_vs_t v_del;

				igraph_vs_vector(&v_del, &deleted_nodes);
				igraph_delete_vertices(&graph_cp, v_del);

				/* GRAPH FINAL INFORMATION */
				int n_comp;
				igraph_clusters(&graph_cp, NULL, &comp, &n_comp, IGRAPH_WEAK);
				long final_L_comp = igraph_vector_max(&comp);
				cout << "Final Number of Components: " << n_comp << "\nLargest Component: " << final_L_comp << endl;
				cout << "Final Average Degree: " << (2.0 * igraph_ecount(&graph_cp) / igraph_vcount(&graph_cp)) << endl;
				
				fprintf(output_file, "\nN_COMP %d\n", n_comp);
				fprintf(output_file, "L_COMP %ld\n", final_L_comp);
				fprintf(output_file, "D_FINAL %f\n", (2.0 * igraph_ecount(&graph_cp) / igraph_vcount(&graph_cp)));

				int unconn_pairs = 0;

				igraph_shortest_paths(&graph_cp, &m, igraph_vss_all(), igraph_vss_all(), IGRAPH_ALL);

				long rows = igraph_matrix_nrow(&m);
				long cols = igraph_matrix_ncol(&m);

				for (int row = 0; row < rows; row++) {
					for (int col = 0; col < cols; col++) {
						if (MATRIX(m, row, col) == IGRAPH_INFINITY)
							unconn_pairs++;
					}
				}

				unconn_pairs /= 2;

				cout << "Number of unconnected pairs of vertices: " << unconn_pairs << endl;

				fprintf(output_file, "UNCONN_PAIRS %d\n", unconn_pairs);

				igraph_destroy(&graph_cp);
				igraph_vector_clear(&deleted_nodes);
			
			}
			igraph_vector_destroy(&capacity_cp);

		}
		igraph_destroy(&graph);
		initial_nodes.clear();

	}

	fclose(output_file);

	// Free memory
	igraph_vector_destroy(&capacity);
	igraph_vector_destroy(&deletion_list);
	igraph_vector_destroy(&del_edges);
	igraph_vector_destroy(&curr_bc);
	igraph_vector_destroy(&comp);
	igraph_vector_destroy(&capacity_sorted);
	igraph_vector_destroy(&degree_sorted);
	igraph_vector_destroy(&clustering_sorted);
	igraph_vector_destroy(&degree);
	igraph_vector_destroy(&clustering);
	igraph_matrix_destroy(&m);
	igraph_vector_destroy(&deleted_nodes);

	return 0;

}