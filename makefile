all: cascade_node cascade_edge sim

cascade_node: Simulations/cascade_node.C
	g++ -std=c++11 Simulations/cascade_node.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/cascade_node

cascade_edge: Simulations/cascade_edge.C
	g++ -std=c++11 Simulations/cascade_edge.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/cascade_edge

sim: Animation/sim.C
	g++ -std=c++11 Animation/sim.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/sim

ricky: cascade_node_r cascade_edge_r sim_r

CC = g++
CFLAGS = -std=c++11 -g
LIBS = -ligraph -lm -lstdc++ -lxml2 -lz -lgmp -lblas -lcxsparse -lglpk -llapack -larpack -lgomp -lpthread
LIBS_PATHS = -I/usr/local/include/igraph -L/usr/local/lib
GRAPHIC_LIBS = -lpython3.8
GRAPHIC_PATHS = -I/usr/include/python3.8 -I/home/ricky/.local/lib/python3.8/site-packages/numpy/core/include

cascade_node_r: Simulations/cascade_node.C
	$(CC) $(CFLAGS) Simulations/cascade_node.C $(LIBS_PATHS) $(LIBS) -o Executables/cascade_node

cascade_edge_r: Simulations/cascade_edge.C
	$(CC) $(CFLAGS) Simulations/cascade_edge.C $(LIBS_PATHS) $(LIBS) -o Executables/cascade_edge

sim_r: Animation/sim.C
	$(CC) $(CFLAGS) Animation/sim.C $(LIBS_PATHS) $(LIBS) -o Executables/sim