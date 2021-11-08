#include <igraph.h>
#include <time.h>
#include "matplotlibcpp.h"

namespace plt = matplotlibcpp;
using namespace std;

int main(int argc, char** argv) {

    igraph_t graph;
    igraph_real_t apl, c, L0, C0;
    int n_pts = 100;
    vector<double> powerlaw(50, 0);
    vector<int> deg(50);
    vector<double> degree_freq(n_pts,0);
    vector<int> degree(n_pts);
    for(int i = 0; i < n_pts; degree[i] = i, ++i);

    int cummulative_vcount = 0;

    for(int i = 0; i < 10; ++i) {
        char filename[50] = {0};
        sprintf(filename, "Simulations/graphs/%s_%d.gml", argv[1], i);    
        FILE *input_file = fopen(filename, "r");
        if (input_file == 0) {
            cout << "Unable to open input file " << filename << ". Exiting\n";
            return 11;
        }
        igraph_read_graph_gml(&graph, input_file);
        igraph_vector_t result;
        igraph_vector_init(&result, n_pts);

        igraph_degree(&graph, &result, igraph_vss_all(), IGRAPH_ALL, IGRAPH_NO_LOOPS);
        for(int k = 0; k < igraph_vcount(&graph); ++k)
            if(VECTOR(result)[k] < n_pts)
                ++degree_freq[VECTOR(result)[k]];
        
        cummulative_vcount += igraph_vcount(&graph);
        fclose(input_file);
    }
    for(int k = 0; k < n_pts; ++k)
        degree_freq[k] /= (cummulative_vcount);
    for(int k = 0; k < 50; ++k) {
        deg[k] = k + 2;
        powerlaw[k] = 4*pow(k + 2, -3);
    }


    plt::figure();
    // plt::loglog(degree, degree_freq, "-o");
    plt::plot(degree, degree_freq, "-o");
    // plt::loglog(deg, powerlaw, "g--");
    plt::grid(true);
    // plt::legend();
    plt::xlabel("$Degree$");
    plt::ylabel("$Frequency$");
    char plt_title[50] = {0};
    sprintf(plt_title, "%s Average Degree Distribution", argv[1]);
    plt::title(plt_title);
    plt::show();
    // plt::save("mygraph.png");

    igraph_destroy(&graph);
    return 0;
}