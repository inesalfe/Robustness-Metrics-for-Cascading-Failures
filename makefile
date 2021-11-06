# Inês

all: cascade_node ba sim ba_sim small p_law2 p_law4 test_nets random cascade_node_realnet

cascade_node: Simulations/cascade_node.C
	g++ -std=c++11 -O3 Simulations/cascade_node.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/cascade_node

cascade_node_realnet: Simulations/cascade_node_realnet.C
	g++ -std=c++11 -O3 Simulations/cascade_node_realnet.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/cascade_node_realnet

p_law2: Simulations/p_law2.C
	g++ -std=c++11 -O3 Simulations/p_law2.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/p_law2

p_law4: Simulations/p_law4.C
	g++ -std=c++11 -O3 Simulations/p_law4.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/p_law4

random: Simulations/random.C
	g++ -std=c++11 -O3 Simulations/random.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/random

ws: Simulations/ws.C
	g++ -std=c++11 -O3 Simulations/ws.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/ws

ba: Simulations/ba.C
	g++ -std=c++11 -O3 Simulations/ba.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/ba

p_law: Simulations/p_law.C
	g++ -std=c++11 -O3 Simulations/p_law.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/p_law

test_nets: Simulations/test_nets.C
	g++ -std=c++11 -O3 Simulations/test_nets.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/test_nets

sim: Animation/sim.C
	g++ -std=c++11 -O3 Animation/sim.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/sim

ba_sim: Animation/Network_Generation/ba.C
	g++ -std=c++11 -O3 Animation/Network_Generation/ba.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/ba_sim

small: Animation/Network_Generation/small.C
	g++ -std=c++11 -O3 Animation/Network_Generation/small.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/small

# Ricardo

ricky: degree_dist #cascade_node_r cascade_node_realnet_r

CC = g++
CFLAGS = -std=c++11 -O3
LIBS = -ligraph -lm -lstdc++ -lxml2 -lz -lgmp -lblas -lcxsparse -lglpk -llapack -larpack -lgomp -lpthread
LIBS_PATHS = -I/usr/local/include/igraph -L/usr/local/lib
GRAPHIC_LIBS = -lpython3.8
GRAPHIC_PATHS = -I/usr/include/python3.8 -I/home/ricky/.local/lib/python3.8/site-packages/numpy/core/include

cascade_node_r: Simulations/cascade_node.C
	$(CC) $(CFLAGS) Simulations/cascade_node.C $(LIBS_PATHS) $(LIBS) -o Executables/cascade_node
	
cascade_node_realnet_r: Simulations/cascade_node_realnet.C
	$(CC) $(CFLAGS) Simulations/cascade_node_realnet.C $(LIBS_PATHS) $(LIBS) -o Executables/cascade_node_realnet

sim_r: Animation/sim.C
	$(CC) $(CFLAGS) Animation/sim.C $(LIBS_PATHS) $(LIBS) -o Executables/sim

degree_dist: Simulations/degree_dist.cpp
	$(CC) $(CFLAGS) Simulations/degree_dist.cpp $(LIBS_PATHS) $(LIBS) $(GRAPHIC_PATHS) $(GRAPHIC_LIBS) -o Simulations/dd

ba_r: Simulations/ba.C
	$(CC) $(CFLAGS) Simulations/ba.C $(LIBS_PATHS) $(LIBS) -o Executables/ba

p_law2_r: Simulations/p_law2.C
	$(CC) $(CFLAGS) Simulations/p_law2.C $(LIBS_PATHS) $(LIBS) -o Executables/p_law2