#include <igraph.h>
#include <time.h>
#include <vector>
#include <iostream>
#include <time.h>

using namespace std;

void print_vector(igraph_vector_t *v) {
	long int i, l = igraph_vector_size(v);
	for (i = 0; i < l; i++) {
		printf("%li ", (long int) VECTOR(*v)[i]);
	}
	printf("\n");
}

int main() {

	
	igraph_t graph; // The graph itself
	igraph_vector_t v; // Auxiliary vector for the edges
	igraph_vector_t deletion_list; 	// List with the vertices to delete - updated in each iteration
	igraph_vector_ptr_t short_paths; // Auxiliary vector for the shorthest paths
	igraph_vector_t comp; // Size of the components
	igraph_vector_t capacity; // The capacity of each vertex equals the initial betweeness centrality
	igraph_vector_t curr_bc; // Betweeness centrality in a given moment
	igraph_es_t del_edges_sel; // Edges to be deleted in each iteration in selector mode
	igraph_vector_t del_edges; // Edges to be deleted in each iteration 
	double alpha = 0;

	// Edges vector where each pair of numbers represents one edge
	igraph_real_t edges[] = {0, 1, 1, 2, 2, 3, 2, 5, 3, 5, 3, 4, 4, 5, 5, 6, 6, 7, 6, 8, 6, 9, 7, 8, 8, 9, 9, 10, 8, 10, 2, 9, 4, 7};
	
	igraph_vector_view(&v, edges, sizeof(edges) / sizeof(double));
	igraph_create(&graph, &v, 0, IGRAPH_UNDIRECTED); // Creation of un undirected graph

	// Write initial network to file GML
    
    FILE * file;

    file = fopen("net.gml", "w");
    if (file == 0) {
        exit(1);
    }

    igraph_write_graph_gml(&graph, file, NULL, 0);
    fclose(file);

	// N is the number of vertices in the network
	igraph_integer_t N = igraph_vcount(&graph);
	cout << endl << "Number of nodes: " << N << endl;
	// N is the number of edges in the network
	igraph_integer_t E = igraph_ecount(&graph);
	cout << "Number of edges: " << E << endl;

	// Initialization of vector to be used
	igraph_vector_init(&capacity, N);
	igraph_vector_init(&curr_bc, N);
	igraph_vector_init(&deletion_list, 0);
	igraph_vector_init(&del_edges, 0);
	igraph_vector_init(&comp, 0);

	// Fill the capacity / load vector
	igraph_betweenness(&graph, &capacity, igraph_vss_all(), IGRAPH_UNDIRECTED, NULL);

	cout << endl << "----------Initial Iteration----------" << endl;

	for(int i = 0; i < igraph_vector_size(&capacity); ++i) {
		cout << "i: " << i << " Load: " << VECTOR(capacity)[i];
		// Define capacity with a tolerance factor alpha
		VECTOR(capacity)[i] = (1+alpha) * VECTOR(capacity)[i];
		cout << " Capacity: " << VECTOR(capacity)[i] << endl;;
	}

	// Choose random vertex to delete
	srandom(time(NULL));
	int initial_node = random()%N;
	igraph_vector_push_back(&deletion_list, initial_node);
	cout << "Delete " << initial_node << endl << endl;

	while(!igraph_vector_empty(&deletion_list)) {

		cout << "----------New Iteration----------" << endl;

		// Write in files the "deleted" vertices

		// Delete edges incident in the vertices in the deletion list
		while(!igraph_vector_empty(&deletion_list)) {
			igraph_incident(&graph, &del_edges, igraph_vector_pop_back(&deletion_list), IGRAPH_ALL);
			// print_vector(&del_edges);
			igraph_es_vector(&del_edges_sel, &del_edges);
			igraph_delete_edges(&graph, del_edges_sel);
		}

		// Recalculate the betweeness centralities
		igraph_betweenness(&graph, &curr_bc, igraph_vss_all(), IGRAPH_UNDIRECTED, NULL);

		// Create new deletion_list
		for(int i = 0; i < igraph_vector_size(&curr_bc); ++i) {
			cout << "i: " << i << " Current Load: " << VECTOR(curr_bc)[i] << " Capacity: " << VECTOR(capacity)[i] << endl;
			if (VECTOR(curr_bc)[i] > VECTOR(capacity)[i]) {
				cout << "Delete " << i << endl;
				igraph_vector_push_back(&deletion_list, i);
			}
		}

		cout << endl;
	}

	igraph_integer_t n_comp; // Number of connected components
	igraph_clusters(&graph, NULL, &comp, &n_comp, IGRAPH_WEAK);
	// Sizes of the components
	cout << "Sizes of the connected components:" << endl;
	print_vector(&comp);
	cout << "Number of connected components: " << n_comp << endl;

	igraph_vector_destroy(&capacity);
	igraph_vector_destroy(&curr_bc);
	igraph_destroy(&graph);
	igraph_vector_destroy(&comp);
	igraph_vector_destroy(&deletion_list);
	igraph_vector_destroy(&del_edges);

    return 0;

}