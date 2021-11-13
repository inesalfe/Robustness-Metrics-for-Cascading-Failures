sims: sim
all: cascade_node ba sim ba_sim small p_law2 p_law4 test_nets random cascade_node_realnet

CC = g++
CFLAGS = -std=c++11 -O3
LIBS_PATHS = -I/usr/local/include/igraph -L/usr/local/lib

# For MacOS
# LIBS = -ligraph

# For WSL
LIBS = -ligraph -lm -lstdc++ -lxml2 -lz -lgmp -lblas -lcxsparse -lglpk -llapack -larpack -lgomp -lpthread

cascade_node: Simulations/cascade_node.C
	$(CC) $(CFLAGS) Simulations/cascade_node.C $(LIBS_PATHS) $(LIBS) -o Executables/cascade_node

cascade_node_realnet: Simulations/cascade_node_realnet.C
	$(CC) $(CFLAGS) Simulations/cascade_node_realnet.C $(LIBS_PATHS) $(LIBS) -o Executables/cascade_node_realnet

p_law2: Simulations/p_law2.C
	$(CC) $(CFLAGS) Simulations/p_law2.C $(LIBS_PATHS) $(LIBS) -o Executables/p_law2

p_law4: Simulations/p_law4.C
	$(CC) $(CFLAGS) Simulations/p_law4.C $(LIBS_PATHS) $(LIBS) -o Executables/p_law4

random: Simulations/random.C
	$(CC) $(CFLAGS) Simulations/random.C $(LIBS_PATHS) $(LIBS) -o Executables/random

ws: Simulations/ws.C
	$(CC) $(CFLAGS) Simulations/ws.C $(LIBS_PATHS) $(LIBS) -o Executables/ws

ba: Simulations/ba.C
	$(CC) $(CFLAGS) Simulations/ba.C $(LIBS_PATHS) $(LIBS) -o Executables/ba

p_law: Simulations/p_law.C
	$(CC) $(CFLAGS) Simulations/p_law.C $(LIBS_PATHS) $(LIBS) -o Executables/p_law

test_nets: Simulations/test_nets.C
	$(CC) $(CFLAGS) Simulations/test_nets.C $(LIBS_PATHS) $(LIBS) -o Executables/test_nets

sim: Animation/sim.C
	$(CC) $(CFLAGS) Animation/sim.C $(LIBS_PATHS) $(LIBS) -o Executables/sim

ba_sim: Animation/Network_Generation/ba.C
	$(CC) $(CFLAGS) Animation/Network_Generation/ba.C $(LIBS_PATHS) $(LIBS) -o Executables/ba_sim

small: Animation/Network_Generation/small.C
	$(CC) $(CFLAGS) Animation/Network_Generation/small.C $(LIBS_PATHS) $(LIBS) -o Executables/small