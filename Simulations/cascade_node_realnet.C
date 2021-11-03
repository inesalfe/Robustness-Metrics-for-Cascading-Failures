#include <igraph.h>
#include <vector>
#include <iostream>
#include <string.h>

using namespace std;

#define IT 5 // Iterations of the same network per alpha

// Auxiliary function to print an igraph_vector
void print_vector(igraph_vector_t *v) {
	long int i, l = igraph_vector_size(v);
	for (i = 0; i < l; i++)
		printf("%li ", (long int) VECTOR(*v)[i]);
	printf("\n");
}

int main() {

	// The user inserts the model of the network
	cout << "Please choose the model:" << endl;
	cout << "0 - Power Grid" << endl;
	cout << "1 - Internet" << endl;

	int model;
	cin >> model;
	while(cin.fail() || model < 0 || model > 1) {
		cout << "Invalid Input" << endl;
		cin.clear();
		cin.ignore(256,'\n');
		cin >> model;
	}

	// The user inserts the criterion for node deletion
	cout << "Please choose the criterion for node eliminatiton:" << endl;
	cout << "0 - RANDOM" << endl;
	cout << "1 - HIGHEST LOAD (BETWEENNESS CENTRALITY)" << endl;
	cout << "2 - HIGHEST AVERAGE DEGREE" << endl;
	cout << "3 - HIGHEST CLUSTERING COEFICIENT" << endl;

	int criterion;
	cin >> criterion;
	while(cin.fail() || criterion < 0 || criterion > 3) {
		cout << "Invalid Input" << endl;
		cin.clear();
		cin.ignore(256,'\n');
		cin >> criterion;
	}

	// Choose the path for the output files depending on the chosen model and criterion
	char file_name[50] = {0};
	if (model == 0) {
		strcpy(file_name, "Data/PG/data_0.txt");
		file_name[13] = criterion + '0';
	}
	else {
		strcpy(file_name, "Data/INT/data_0.txt");
		file_name[14] = criterion + '0';
	}

	FILE *output_file = fopen(file_name, "w");
	if (output_file == 0) {
		cout << "Unable to open output file " << file_name << ". Exiting\n";
		return 10;
	}

	igraph_t graph, graph_cp; // The graph itself
	igraph_vector_t deletion_list; 	// List with the vertices to delete - updated in each iteration
	igraph_vector_t del_edges; // Edges to be deleted in each iteration
	igraph_vector_t deleted_nodes; 	// List with the deleted nodes in each iteration
	igraph_vector_t comp; // Size of the components
	igraph_vector_t capacity; // The capacity of each vertex equals the initial betweeness centrality
	igraph_vector_t capacity_cp; // The capacity of each vertex equals the initial betweeness centrality
	igraph_vector_t capacity_sorted; // Sorted capacity
	igraph_vector_t curr_bc; // Betweeness centrality in a given moment
	igraph_vector_t degree_sorted; // Sorted degree of each vertex
	igraph_vector_t clustering_sorted; // Sorted clustering coeficient of each vertex
	igraph_vector_t degree; // Degree of each vertex
	igraph_vector_t clustering; // Clustering coeficient of each vertex
	igraph_matrix_t m; // Matrix to hold the shortest path between each pair of nodes
	igraph_vector_ptr_t short_paths; // Auxiliary vector for the shorthest paths
	igraph_es_t del_edges_sel; // Edges to be deleted in each iteration in selector mode
	vector<long> initial_nodes; // Vector with the nodes to be deleted in each iteration

	// Initializations
	igraph_rng_seed(igraph_rng_default(), 0);
	igraph_vector_init(&comp, 0);
	igraph_vector_init(&capacity, 0);
	igraph_vector_init(&curr_bc, 0);
	igraph_vector_init(&deletion_list, 0);
	igraph_vector_init(&del_edges, 0);
	igraph_vector_init(&degree, 0);
	igraph_vector_init(&clustering, 0);
	igraph_vector_init(&deleted_nodes, 0);
	igraph_matrix_init(&m, 0, 0);

	// Choose the path for the input files
	if (model == 0) {
		char filename[50] = "Simulations/Graphs/power.gml";

		FILE *input_file = fopen(filename, "r");
		if (input_file == 0) {
			cout << "Unable to open input file " << filename << ". Exiting\n";
			return 11;
		}

		igraph_read_graph_gml(&graph, input_file);
		fclose(input_file);
	}
	else {
		char filename[50] = "Simulations/Graphs/as-22july06.gml";

		FILE *input_file = fopen(filename, "r");
		if (input_file == 0) {
			cout << "Unable to open input file " << filename << ". Exiting\n";
			return 11;
		}

		igraph_read_graph_gml(&graph, input_file);
		fclose(input_file);
	}

	int N = igraph_vcount(&graph);

	// Printing general information in the output file
	fprintf(output_file, "N %d\n", N);
	fprintf(output_file, "N_NET %d\n", 1);
	fprintf(output_file, "IT %d\n", IT);
	fprintf(output_file, "CRITERIA %d\n", criterion);
	fprintf(output_file, "ALPHAS");

	// Filling the alphas vector
	vector<double> alphas(11);
	vector<vector<double>> ratios(11, vector<double>(10,0));
	for(int i = 0; i < 11; ++i) {
		alphas[i] = .1 * i;
		fprintf(output_file, " %.1f", alphas[i]);
	}

	fprintf(output_file, "\n");

	/* GRAPH INITIAL INFORMATION */
	cout << "Number of Nodes: " << N << endl;
	cout << "Average Degree: " << (2.0 * igraph_ecount(&graph) / N) << endl;

	/* CAPACITY METRIC - Betweeness centrality - O(|V||E|) */
	igraph_betweenness(&graph, &capacity, igraph_vss_all(), IGRAPH_UNDIRECTED, NULL);

	/* CHOOSE INITIAL VERTEX TO DELETE... */
	long initial_node;
	switch (criterion) {
		case 0:
			// ... RANDOMLY
			srandom(time(NULL));
			for (int i = 0; i < IT; i++) {
				initial_nodes.push_back(random() % N);
			}
			break;
		case 1:
			// ... HIGHEST LOAD - O(|V| log |V|)
			igraph_vector_copy(&capacity_sorted, &capacity);
			igraph_vector_reverse_sort(&capacity_sorted);
			for (int i = 0; i < IT; i++) {
				igraph_vector_search(&capacity, 0, VECTOR(capacity_sorted)[i], &initial_node);
				initial_nodes.push_back(initial_node);
			}
			igraph_vector_destroy(&capacity_sorted);
			break;
		case 2:
			// ... HIGHEST AVERAGE DEGREE - O(|V| log |V|)
			igraph_degree(&graph, &degree, igraph_vss_all(), IGRAPH_ALL, false);
			igraph_vector_copy(&degree_sorted, &degree);
			igraph_vector_reverse_sort(&degree_sorted);
			for (int i = 0; i < IT; i++) {
				igraph_vector_search(&degree, 0, VECTOR(degree_sorted)[i], &initial_node);
				initial_nodes.push_back(initial_node);
			}
			igraph_vector_destroy(&degree_sorted);
			break;
		case 3:
			// ... HIGHEST CLUSTERING COEFICIENT - O(|V| log |V|)
			igraph_transitivity_local_undirected(&graph, &clustering, igraph_vss_all(), IGRAPH_TRANSITIVITY_ZERO); // O(|V|*<k>^2)
			igraph_vector_copy(&clustering_sorted, &clustering);
			igraph_vector_reverse_sort(&clustering_sorted);
			for (int i = 0; i < IT; i++) {
				igraph_vector_search(&clustering, 0, VECTOR(clustering_sorted)[i], &initial_node);
				initial_nodes.push_back(initial_node);
			}
			igraph_vector_destroy(&clustering_sorted);
			break;
	}

	/* FOR EACH NETWORK RUN FOR EACH ALPHA */
	for(int a = 0; a < 11; ++a) {
		
		cout << "########## ALPHA = " << alphas[a] <<  " ##########" << endl;

		igraph_vector_copy(&capacity_cp, &capacity);

		/* SCALE CAPACITY BY alpha */
		igraph_vector_scale(&capacity_cp, (igraph_real_t) (1 + alphas[a]));

		for(int it = 0; it < IT; ++it) {

			cout << endl << "##### Iteration " << it + 1 << "/" << IT << " #####" << endl;
			
			// Create a copy of the original graph so that we can deleted edges and nodes safely
			igraph_copy(&graph_cp, &graph);

			// Fill the deletion list with the first node to be deleted
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
				for(int i = 0; i < N; ++i) {
					if (VECTOR(curr_bc)[i] > VECTOR(capacity_cp)[i]) {
						igraph_vector_push_back(&deletion_list, i);
					}
				}
			}

			// PRINT THE TOTAL NUMBER OF CASCADING ITERATIONS
			cout << endl << "Iterations: " << iterations << endl << endl;
			
			fprintf(output_file, "\nITER %d", iterations);

			/* DELETE THE REMOVED NODES FROM THE NETWORK SO THAT WE CAN COMPUTE SEVERAL METRICS */
			igraph_vs_t v_del;

			igraph_vs_vector(&v_del, &deleted_nodes);
			igraph_delete_vertices(&graph_cp, v_del);

			/* GRAPH FINAL INFORMATION */
			int n_comp;
			igraph_clusters(&graph_cp, NULL, &comp, &n_comp, IGRAPH_WEAK);
			long final_L_comp = igraph_vector_max(&comp);
			cout << "Final Number of Components: " << n_comp << "\nLargest Component: " << final_L_comp << endl;
			cout << "Final Average Degree: " << (2.0 * igraph_ecount(&graph_cp) / N) << endl;
			
			fprintf(output_file, "\nN_COMP %d\n", n_comp);
			fprintf(output_file, "L_COMP %ld\n", final_L_comp);
			fprintf(output_file, "D_FINAL %f\n", (2.0 * igraph_ecount(&graph_cp) / N));

			// Get the number of unconnected pairs of nodes in the network
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

	fclose(output_file);

	// Free memory
	igraph_vector_destroy(&capacity);
	igraph_vector_destroy(&deletion_list);
	igraph_vector_destroy(&del_edges);
	igraph_vector_destroy(&curr_bc);
	igraph_vector_destroy(&comp);
	igraph_vector_destroy(&degree);
	igraph_vector_destroy(&clustering);
	igraph_matrix_destroy(&m);
	igraph_vector_destroy(&deleted_nodes);

	return 0;

}