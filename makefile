cascade: Simulations/cascade.C
	g++ -std=c++11 Simulations/cascade.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/cascade

sim: Animation/sim.C
	g++ -std=c++11 Animation/sim.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o Executables/sim