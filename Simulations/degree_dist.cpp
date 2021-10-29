#include <igraph.h>
#include <time.h>
#include "matplotlibcpp.h"

namespace plt = matplotlibcpp;
using namespace std;

int main() {

    igraph_t graph;
    igraph_real_t apl, c, L0, C0;
    int n_pts = 100;
    vector<double> powerlaw(20, 0);
    vector<int> deg(20);
    vector<double> degree_freq(n_pts,0);
    vector<int> degree(n_pts);
    for(int i = 0; i < n_pts; degree[i] = i, ++i);

    FILE *input_file = fopen("Simulations/Graphs/lfr.gml", "r");
    if (input_file == 0) {
        cout << "Unable to open input file Simulations/Graphs/lfr.gml. Exiting\n";
        return 11;
    }
    igraph_read_graph_gml(&graph, input_file);
    igraph_vector_t result;
    igraph_vector_init(&result, n_pts);

    igraph_degree(&graph, &result, igraph_vss_all(), IGRAPH_ALL, IGRAPH_NO_LOOPS);
    for(int k = 0; k < igraph_vcount(&graph); ++k)
        if(VECTOR(result)[k] < n_pts)
            ++degree_freq[VECTOR(result)[k]];
    for(int k = 0; k < n_pts; ++k)
        degree_freq[k] /= igraph_vcount(&graph);
    for(int k = 0; k < 20; ++k) {
        deg[k] = k + 2;
        powerlaw[k] = 8*pow(k + 2, -3);
    }

    plt::figure();
    plt::loglog(degree, degree_freq, "-o");
    plt::loglog(deg, powerlaw, "g--");
    plt::grid(true);
    // plt::legend();
    plt::xlabel("$Degree$");
    plt::ylabel("$Frequency$");
    plt::title("LFR Degree Distributions");
    plt::show();
    // plt::save("mygraph.png");

    igraph_destroy(&graph);
    return 0;
}