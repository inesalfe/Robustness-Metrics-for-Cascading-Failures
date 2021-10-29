#include <igraph.h>
#include <vector>
#include <iostream>

using namespace std;

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
	cout << "0 - Barabasi Albert Model" << endl;
	cout << "1 - DMS Minimal Model" << endl;
	cout << "2 - Small example Network" << endl;

	int model;
	cin >> model;
	while(cin.fail() || model < 0 || model > 2) {
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
	char file_name[30] = {0};
	if (model == 0) {
		strcpy(file_name, "Animation/Data/ba_0.txt");
		file_name[18] = criterion + '0';
	}
	else if (model == 1) {
		strcpy(file_name, "Animation/Data/dms_0.txt");
		file_name[19] = criterion + '0';
	}
	else {
		strcpy(file_name, "Animation/Data/small_0.txt");
		file_name[21] = criterion + '0';
	}

	FILE *output_file = fopen(file_name, "w");
	if (output_file == 0) {
		cout << "Unable to open output file " << file_name << ". Exiting\n";
		return 10;
	}

	igraph_t graph; // The graph itself

	// Choose the path for the input files
	if (model == 0) {
		char filename[50] = {0};
		strcpy(filename, "Animation/Graphs/ba.gml");

		FILE *input_file = fopen(filename, "r");
		if (input_file == 0) {
			cout << "Unable to open input file " << filename << ". Exiting\n";
			return 11;
		}

		igraph_read_graph_gml(&graph, input_file);
		fclose(input_file);
	}
	else if (model == 1) {
		char filename[50] = {0};
		strcpy(filename, "Animation/Graphs/dms.gml");

		FILE *input_file = fopen(filename, "r");
		if (input_file == 0) {
			cout << "Unable to open input file " << filename << ". Exiting\n";
			return 11;
		}

		igraph_read_graph_gml(&graph, input_file);
		fclose(input_file);
	}
	else {
		char filename[50] = {0};
		strcpy(filename, "Animation/Graphs/small.gml");

		FILE *input_file = fopen(filename, "r");
		if (input_file == 0) {
			cout << "Unable to open input file " << filename << ". Exiting\n";
			return 11;
		}

		igraph_read_graph_gml(&graph, input_file);
		fclose(input_file);
	}

	int N = igraph_vcount(&graph);

	double alpha = 0;

	igraph_vector_t deletion_list; 	// List with the vertices to delete - updated in each iteration
	igraph_vector_t capacity; // The capacity of each vertex equals the initial betweeness centrality
	igraph_vector_t capacity_cp; // The capacity of each vertex equals the initial betweeness centrality
	igraph_vector_t curr_bc; // Betweeness centrality in a given moment
	igraph_vector_t degree; // Degree of each vertex
	igraph_vector_t clustering; // Clustering coeficient of each vertex
	igraph_vector_t del_edges; // Clustering coeficient of each vertex
	igraph_es_t del_edges_sel; // Edges to be deleted in each iteration in selector mode
	igraph_vector_t edges_v; // Edges to be deleted in each iteration - each pair of vertices corresponds to one edge

	// Initializations
	igraph_rng_seed(igraph_rng_default(), 0);
	igraph_vector_init(&capacity, N);
	igraph_vector_init(&curr_bc, N);
	igraph_vector_init(&deletion_list, 0);
	igraph_vector_init(&degree, N);
	igraph_vector_init(&clustering, N);
	igraph_vector_init(&del_edges, 0);
	igraph_vector_init(&edges_v, 0);

	/* CAPACITY METRIC - Betweeness centrality */
	igraph_betweenness(&graph, &capacity, igraph_vss_all(), IGRAPH_UNDIRECTED, NULL);

	/* CHOOSE INITIAL VERTEX TO DELETE... */
	long initial_node;
	switch (criterion) {
		case 0:
			// ... RANDOMLY
			srandom(time(NULL));
			initial_node = random() % N;
			break;
		case 1:
			// ... HIGHEST LOAD
			initial_node = igraph_vector_which_max(&capacity);
			break;
		case 2:
			// ... HIGHEST AVERAGE DEGREE
			igraph_degree(&graph, &degree, igraph_vss_all(), IGRAPH_ALL, false);
			initial_node = igraph_vector_which_max(&degree);
			break;
		case 3:
			// ... HIGHEST CLUSTERING COEFICIENT
			igraph_transitivity_local_undirected(&graph, &clustering, igraph_vss_all(), IGRAPH_TRANSITIVITY_ZERO);
			initial_node = igraph_vector_which_max(&clustering);
			break;
	}

	/* SCALE CAPACITY BY alpha */
	igraph_vector_copy(&capacity_cp, &capacity);
	igraph_vector_scale(&capacity_cp, (igraph_real_t) (1 + alpha));

	// Fill the deletion list with the first node to be deleted
	igraph_vector_push_back(&deletion_list, initial_node);

	/* MAIN LOOP */
	int it = 1;
	while(!igraph_vector_empty(&deletion_list)) {

		fprintf(output_file, "it %d\n", it);

		// Delete edges incident in the vertices in the deletion list
		while(!igraph_vector_empty(&deletion_list)) {
			fprintf(output_file, "%d\n", int(VECTOR(deletion_list)[igraph_vector_size(&deletion_list)-1]));
			
			igraph_incident(&graph, &del_edges, igraph_vector_pop_back(&deletion_list), IGRAPH_ALL);
			igraph_es_vector(&del_edges_sel, &del_edges);

			igraph_edges(&graph, del_edges_sel, &edges_v);
			for (int i = 0; i < igraph_vector_size(&edges_v); i++) {
				fprintf(output_file, "%d ", int(VECTOR(edges_v)[i]));
			}
			fprintf(output_file, "\n");

			igraph_delete_edges(&graph, del_edges_sel);
		}

		// Recalculate the betweeness centralities
		igraph_betweenness(&graph, &curr_bc, igraph_vss_all(), IGRAPH_UNDIRECTED, NULL);
		
		// Create new deletion_list
		for(int i = 0; i < igraph_vector_size(&curr_bc); ++i) {
			if (VECTOR(curr_bc)[i] > VECTOR(capacity_cp)[i]) {
				igraph_vector_push_back(&deletion_list, i);
			}
		}

		it++;

	}

	fclose(output_file);

	// Free memory
	igraph_destroy(&graph);
	igraph_vector_destroy(&capacity);
	igraph_vector_destroy(&capacity_cp);
	igraph_vector_destroy(&deletion_list);
	igraph_vector_destroy(&del_edges);
	igraph_vector_destroy(&curr_bc);
	igraph_vector_destroy(&degree);
	igraph_vector_destroy(&clustering);

	return 0;

}