cascade_node: Simulations/cascade_node.C
	g++ -std=c++11 Simulations/cascade_node.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/cascade_node

cascade_edge: Simulations/cascade_edge.C
	g++ -std=c++11 Simulations/cascade_edge.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/cascade_edge

sim: Animation/sim.C
	g++ -std=c++11 Animation/sim.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/sim