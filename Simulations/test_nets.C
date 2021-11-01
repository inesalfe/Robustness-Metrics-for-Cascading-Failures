#include <igraph.h>
#include <vector>
#include <iostream>
#include <string.h>

using namespace std;

#define N_GRAPHS 10

int main() {

	int N = 5000;

	char f_name1[50] = {0};
	strcpy(f_name1, "Data/first_line_2.txt");

	FILE *file1 = fopen(f_name1, "w");
	if (file1 == 0) {
		cout << "Unable to open output file " << f_name1 << ". Exiting\n";
		return 10;
	}

	fprintf(file1, "N");

	for(int n = 0; n < N_GRAPHS; ++n) {

		char filename[50] = {0};
		sprintf(filename, "Simulations/Graphs/pl2_%d.gml", n);

		FILE *input_file = fopen(filename, "r");
		if (input_file == 0) {
			cout << "Unable to open input file " << filename << ". Exiting\n";
			return 11;
		}

		igraph_t graph;

		igraph_read_graph_gml(&graph, input_file);
		fclose(input_file);

		N = igraph_vcount(&graph);

		fprintf(file1, " %d", N);
		
		cout << N << endl;
	}

	fprintf(file1, "\n");

	fclose(file1);

	char f_name2[50] = {0};
	strcpy(f_name2, "Data/first_line_4.txt");

	FILE *file2 = fopen(f_name2, "w");
	if (file2 == 0) {
		cout << "Unable to open output file " << f_name2 << ". Exiting\n";
		return 10;
	}

	fprintf(file2, "N");

	for(int n = 0; n < N_GRAPHS; ++n) {

		char filename[50] = {0};
		sprintf(filename, "Simulations/Graphs/pl4_%d.gml", n);

		FILE *input_file = fopen(filename, "r");
		if (input_file == 0) {
			cout << "Unable to open input file " << filename << ". Exiting\n";
			return 11;
		}

		igraph_t graph;

		igraph_read_graph_gml(&graph, input_file);
		fclose(input_file);

		N = igraph_vcount(&graph);

		fprintf(file2, " %d", N);
		
		cout << N << endl;
	}

	fprintf(file2, "\n");

	fclose(file2);

	return 0;
}

