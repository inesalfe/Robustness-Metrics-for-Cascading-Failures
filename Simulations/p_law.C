#include <igraph.h>
#include <iostream>

using namespace std;

int main() {

	int N;
	double K;

	igraph_t graph; // The graph itself
	igraph_vector_t clusters;
	igraph_vector_t comp; // Size of the components
	igraph_vector_t deleted_nodes; // Size of the components

	igraph_vector_init(&clusters, 0);
	igraph_vector_init(&comp, 0);
	igraph_vector_init(&deleted_nodes, 0);

	// Path to the output file
	char file_name[28] = "Simulations/Graphs/pl_0.gml";

	int file_counter = 0;

	// FIRST NETWORK

	igraph_rng_seed(igraph_rng_default(), 0);

	N = 100000;
	K = 0.5;

	FILE * file;

	// Change path name according to the network
	file_name[22] = file_counter + '0';

	file = fopen(file_name, "w");
	if (file == 0) {
		exit(1);
	}

	igraph_static_power_law_game(&graph, N, N*K/2, 3, -1, false, false, true);
		
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

	if (avgd > 1.985 && avgd < 2.015 && igraph_vcount(&graph) > 4950 && igraph_vcount(&graph) < 5050) {
		cout << "Number of nodes: " << igraph_vcount(&graph) << endl;
		cout << "Number of components: " << n_comp << endl;
		cout << "Size of the largest component: " << L_comp_size << endl;
		cout << "Largest component id: " << L_comp << endl;
		cout << "Average degree: " << (2.0 * igraph_ecount(&graph) / igraph_vcount(&graph)) << endl;
	}
	
	igraph_write_graph_gml(&graph, file, NULL, 0);
	
	fclose(file);

	igraph_vector_clear(&clusters);
	igraph_vector_clear(&deleted_nodes);
	igraph_vector_clear(&comp);
	igraph_destroy(&graph);

	file_counter++;

	// SECOND AND THIRD NETWORKS

	igraph_rng_seed(igraph_rng_default(), 0);

	N = 97500;
	K = 0.51;

	for(int n = 0; n < 9; n++) {

		igraph_static_power_law_game(&graph, N, N*K/2, 3, -1, false, false, true);

		if (n == 7 || n == 8) {

			FILE * file;

			// Change path name according to the network
			file_name[22] = file_counter + '0';

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

			if (avgd > 1.985 && avgd < 2.015 && igraph_vcount(&graph) > 4950 && igraph_vcount(&graph) < 5050) {
				cout << "Number of nodes: " << igraph_vcount(&graph) << endl;
				cout << "Number of components: " << n_comp << endl;
				cout << "Size of the largest component: " << L_comp_size << endl;
				cout << "Largest component id: " << L_comp << endl;
				cout << "Average degree: " << (2.0 * igraph_ecount(&graph) / igraph_vcount(&graph)) << endl;
			}
			
			igraph_write_graph_gml(&graph, file, NULL, 0);
			
			fclose(file);

			igraph_vector_clear(&clusters);
			igraph_vector_clear(&deleted_nodes);
			igraph_vector_clear(&comp);

			file_counter++;
		
		}

		igraph_destroy(&graph);

	}

	// FOURTH NETWORK

	igraph_rng_seed(igraph_rng_default(), 0);

	N = 97400;
	K = 0.51;

	for(int n = 0; n < 5; n++) {

		igraph_static_power_law_game(&graph, N, N*K/2, 3, -1, false, false, true);

		if (n == 4) {

			FILE * file;

			// Change path name according to the network
			file_name[22] = file_counter + '0';

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

			if (avgd > 1.985 && avgd < 2.015 && igraph_vcount(&graph) > 4950 && igraph_vcount(&graph) < 5050) {
				cout << "Number of nodes: " << igraph_vcount(&graph) << endl;
				cout << "Number of components: " << n_comp << endl;
				cout << "Size of the largest component: " << L_comp_size << endl;
				cout << "Largest component id: " << L_comp << endl;
				cout << "Average degree: " << (2.0 * igraph_ecount(&graph) / igraph_vcount(&graph)) << endl;
			}
			
			igraph_write_graph_gml(&graph, file, NULL, 0);
			
			fclose(file);

			igraph_vector_clear(&clusters);
			igraph_vector_clear(&deleted_nodes);
			igraph_vector_clear(&comp);

			file_counter++;
		
		}

		igraph_destroy(&graph);

	}

	// FIFTH NETWORK

	igraph_rng_seed(igraph_rng_default(), 0);

	N = 97600;
	K = 0.5;

	for(int n = 0; n < 5; n++) {

		igraph_static_power_law_game(&graph, N, N*K/2, 3, -1, false, false, true);

		if (n == 4) {

			FILE * file;

			// Change path name according to the network
			file_name[22] = file_counter + '0';

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

			if(avgd > 1.985 && avgd < 2.015 && igraph_vcount(&graph) > 4950 && igraph_vcount(&graph) < 5050) {
				cout << "Number of nodes: " << igraph_vcount(&graph) << endl;
				cout << "Number of components: " << n_comp << endl;
				cout << "Size of the largest component: " << L_comp_size << endl;
				cout << "Largest component id: " << L_comp << endl;
				cout << "Average degree: " << (2.0 * igraph_ecount(&graph) / igraph_vcount(&graph)) << endl;
			}
			
			igraph_write_graph_gml(&graph, file, NULL, 0);
			
			fclose(file);

			igraph_vector_clear(&clusters);
			igraph_vector_clear(&deleted_nodes);
			igraph_vector_clear(&comp);

			file_counter++;
		
		}

		igraph_destroy(&graph);

	}

	// SIXTH, SEVENTH AND EIGHTH NETWORKS

	igraph_rng_seed(igraph_rng_default(), 0);

	N = 97800;
	K = 0.51;

	for(int n = 0; n < 41; n++) {

		igraph_static_power_law_game(&graph, N, N*K/2, 3, -1, false, false, true);

		if (n == 6 || n == 35 || n == 40) {

			FILE * file;

			// Change path name according to the network
			file_name[22] = file_counter + '0';

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

			if (avgd > 1.985 && avgd < 2.015 && igraph_vcount(&graph) > 4950 && igraph_vcount(&graph) < 5050) {
				cout << "Number of nodes: " << igraph_vcount(&graph) << endl;
				cout << "Number of components: " << n_comp << endl;
				cout << "Size of the largest component: " << L_comp_size << endl;
				cout << "Largest component id: " << L_comp << endl;
				cout << "Average degree: " << (2.0 * igraph_ecount(&graph) / igraph_vcount(&graph)) << endl;
			}
			
			igraph_write_graph_gml(&graph, file, NULL, 0);
			
			fclose(file);

			igraph_vector_clear(&clusters);
			igraph_vector_clear(&deleted_nodes);
			igraph_vector_clear(&comp);

			file_counter++;
		
		}

		igraph_destroy(&graph);

	}

	// NINETH NETWORK

	igraph_rng_seed(igraph_rng_default(), 0);

	N = 98000;
	K = 0.52;

	for(int n = 0; n < 17; n++) {

		igraph_static_power_law_game(&graph, N, N*K/2, 3, -1, false, false, true);

		if (n == 16) {

			FILE * file;

			// Change path name according to the network
			file_name[22] = file_counter + '0';

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

			if (avgd > 1.985 && avgd < 2.015 && igraph_vcount(&graph) > 4950 && igraph_vcount(&graph) < 5050) {
				cout << "Number of nodes: " << igraph_vcount(&graph) << endl;
				cout << "Number of components: " << n_comp << endl;
				cout << "Size of the largest component: " << L_comp_size << endl;
				cout << "Largest component id: " << L_comp << endl;
				cout << "Average degree: " << (2.0 * igraph_ecount(&graph) / igraph_vcount(&graph)) << endl;
			}
			
			igraph_write_graph_gml(&graph, file, NULL, 0);
			
			fclose(file);

			igraph_vector_clear(&clusters);
			igraph_vector_clear(&deleted_nodes);
			igraph_vector_clear(&comp);

			file_counter++;
		
		}

		igraph_destroy(&graph);

	}

	// TENTH NETWORK

	igraph_rng_seed(igraph_rng_default(), 0);

	N = 97900;
	K = 0.52;

	for(int n = 0; n < 17; n++) {

		igraph_static_power_law_game(&graph, N, N*K/2, 3, -1, false, false, true);

		if (n == 16) {

			FILE * file;

			// Change path name according to the network
			file_name[22] = file_counter + '0';

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

			if (avgd > 1.985 && avgd < 2.015 && igraph_vcount(&graph) > 4950 && igraph_vcount(&graph) < 5050) {
				cout << "Number of nodes: " << igraph_vcount(&graph) << endl;
				cout << "Number of components: " << n_comp << endl;
				cout << "Size of the largest component: " << L_comp_size << endl;
				cout << "Largest component id: " << L_comp << endl;
				cout << "Average degree: " << (2.0 * igraph_ecount(&graph) / igraph_vcount(&graph)) << endl;
			}
			
			igraph_write_graph_gml(&graph, file, NULL, 0);
			
			fclose(file);

			igraph_vector_clear(&clusters);
			igraph_vector_clear(&deleted_nodes);
			igraph_vector_clear(&comp);

			file_counter++;
		
		}

		igraph_destroy(&graph);

	}

	igraph_vector_destroy(&clusters);
	igraph_vector_destroy(&comp);

	return 0;

}