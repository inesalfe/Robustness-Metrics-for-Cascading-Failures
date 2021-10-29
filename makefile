# Inês

all: cascade_node ba sim ba_sim small

cascade_node: Simulations/cascade_node.C
	g++ -std=c++11 Simulations/cascade_node.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/cascade_node

ba: Simulations/ba.C
	g++ -std=c++11 Simulations/ba.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/ba

sim: Animation/sim.C
	g++ -std=c++11 Animation/sim.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/sim

ba_sim: Animation/Network_Generation/ba.C
	g++ -std=c++11 Animation/Network_Generation/ba.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/ba_sim

small: Animation/Network_Generation/small.C
	g++ -std=c++11 Animation/Network_Generation/small.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/small

# Ricardo

ricky: cascade_node_r sim_r degree_dist ba_r

CC = g++
CFLAGS = -std=c++11 -g
LIBS = -ligraph -lm -lstdc++ -lxml2 -lz -lgmp -lblas -lcxsparse -lglpk -llapack -larpack -lgomp -lpthread
LIBS_PATHS = -I/usr/local/include/igraph -L/usr/local/lib
GRAPHIC_LIBS = -lpython3.8
GRAPHIC_PATHS = -I/usr/include/python3.8 -I/home/ricky/.local/lib/python3.8/site-packages/numpy/core/include

cascade_node_r: Simulations/cascade_node.C
	$(CC) $(CFLAGS) Simulations/cascade_node.C $(LIBS_PATHS) $(LIBS) -o Executables/cascade_node

sim_r: Animation/sim.C
	$(CC) $(CFLAGS) Animation/sim.C $(LIBS_PATHS) $(LIBS) -o Executables/sim

degree_dist: Simulations/degree_dist.cpp
	$(CC) $(CFLAGS) Simulations/degree_dist.cpp $(LIBS_PATHS) $(LIBS) $(GRAPHIC_PATHS) $(GRAPHIC_LIBS) -o Simulations/dd

ba_r: Simulations/ba.C
	$(CC) $(CFLAGS) Simulations/ba.C $(LIBS_PATHS) $(LIBS) -o Executables/ba