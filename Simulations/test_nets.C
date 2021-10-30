#include <igraph.h>
#include <vector>
#include <iostream>
#include <string.h>

using namespace std;

#define N_GRAPHS 10

int main() {

	int N = 5000;

	char f_name[50] = {0};
	strcpy(f_name, "Data/first_line.txt");

	FILE *file = fopen(f_name, "w");
	if (file == 0) {
		cout << "Unable to open output file " << f_name << ". Exiting\n";
		return 10;
	}

	fprintf(file, "N");

	for(int n = 0; n < N_GRAPHS; ++n) {

		char filename[50] = {0};
		sprintf(filename, "Simulations/Graphs/pl_%d.gml", n);

		FILE *input_file = fopen(filename, "r");
		if (input_file == 0) {
			cout << "Unable to open input file " << filename << ". Exiting\n";
			return 11;
		}

		igraph_t graph;

		igraph_read_graph_gml(&graph, input_file);
		fclose(input_file);

		N = igraph_vcount(&graph);

		fprintf(file, " %d", N);
		
		cout << N << endl;
	}

	fprintf(file, "\n");

	fclose(file);

	return 0;
}

