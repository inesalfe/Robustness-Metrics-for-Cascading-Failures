p_law: p_law.C
	g++ -std=c++11 p_law.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o p_law

proj_test_edges: proj_test_edges.C
	g++ -std=c++11 proj_test_edges.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o proj_test_edges

proj_test: proj_test.C
	g++ -std=c++11 proj_test.C -I/usr/local/include/igraph -L/usr/local/lib -ligraph -o proj_test

show: show.C
	gcc show.C -I/usr/local/include/graphviz -L/usr/local/lib -lgvc -lcgraph -lcdt -o show

clean:
	rm proj_test show