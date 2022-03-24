# Robustness Metrics for Cascading Failures

Authors: <br />
	Inês Ferreira, 90395 <br />
	Ricardo Santos, 90178 <br />

This folder contains: <br />
	=> 'Animation' Folder <br />
		o 'Network_Geration' Folder: has the files with the code to generate the networks used in the animations. The corresponding executables (for the C++ files) are in '../../Executables/'. <br />
			- ba.C - C++ code to generate a network from a Barabási-Albert model. <br />
			- dms.py - Python code to generate a network from a DMS Minimal Model. <br />
			- small.C - C++ code to generate a small, artificial, network that shows the working of our algorithm. <br />
		o 'Graphs' Folder: has the networks generated by the files in 'Network_Generation/'. The networks have the same name as the file that generated them. These are .gml files. The .gml files with a 2 appended at the end are the same networks but processed by Gephi to have a given layout. <br />
		o 'Data' Folder: has the files with the results after applying our algorithm to reproduce cascading failures. These will be used to make the animation figures and gifs. <br />
		o 'Figures' Folder: has the figures generated by the anim_nolabels.py and anim_wlabels.py files. These are later combined in a single gif. The suffix '_n', with 0 <= n <= 3, represents the criteria chosen for the first node elimination. <br />
		o 'Gifs' Folder: has the gifs generated by combining the successive figures in the 'Figures/' folder, for each network and each criterion. <br />
		o anim_nolabels.py and anim_wlabels.py - generate the animation figures for the networks in the 'Graphs/' folder with the information in 'Data/'. The latter prints the nodes' labels in the animation (for the smaller network) while the former doesn't. <br />
		o create_gifs.sh - bash script to join the successive figures into a single animated gif, for all the networks and criteria. It requires the 'convert' command. <br />
		o sim.C - C++ code to simulate the cascade of failures. Similar to cascade_node.C. Reads the network graphs from 'Graphs/' and writes the output files with the results to 'Data/'. The corresponding executable is in '../Executables'. <br />
	=> 'Data' Folder: has several folders with the data resulting from applying the cascade failures algorithm (cascade_node.C file). These data files are then used by the .py files in 'Plots' to create several plots with the results and metrics. Each folder represents a type of network and each folder has 4 files, one for each attack criteria. The remaining files are only auxiliary, with the number of nodes (for networks with a variable number of nodes, namely the powerlaws and the random network). <br />
	=> 'Executables' Folder: has all the executable files (resulting from the compilation of all the C++ files). <br />
	=> 'Plots' Folder: has the .py files used to create the plots that show the results from the cascading algorithm. Each python file reads the data from the corresponding data file in 'Data/'. Each file plots a different metric: apl_nodes.py - number of unconnected pair of nodes; final_n.py - final number of nodes; giant_c_nodes.py - initial and final giant components ratio; iterations.py - number of iterations of the algorithm; n_comp_nodes.py - number of connected components in the network after the termination of the algorithm; node_deletion.py - number of nodes deleted in each iteration. Each plot is saved in the 'figures/' folder. 'figures/' folder has all the images shown in our report paper. <br />
	=> 'Simulations' Folder: <br />
		o ba.C, dms.py, p_law2.C, p_law4.C, random.C, test_nets.C and ws.C - Files to generate the used networks. These networks are saved in the 'Graphs/' folder. The corresponding executables (for the C++ files) are in '../Executables/'. <br />
		o cascade_node.C and cascade_node_realnet.C - files that implement the developed cascading failures algorithm. These files allow the choice of the network to consider and the choice of the elimination criteria. The latter is similar to the former, but from the two real networks considered the Internet and Power Grid. The corresponding executables are in '../Executables/'. v
		o 'Graphs' Folder: has all the .gml files containing the networks that were used throughout the project. Each type of network has 10 different instances (appended with '_n', n \in [0,9]), corresponding to 10 different seeds, except for the real-world networks, as-22july06.gml (Internet) and power.gml (Power Grid). <br />
		o degree_dist.py - plots the average degree distribution for a user-selected network for those in 'Graphs'. The resulting plots are in '../Plots/figures/'. <br />
		
	=> makefile: Compiles all the C++ files. The resulting executables are sent to the 'Executables/' folder. <br />

Usage: <br />
	To compile the code C++ (even though all the executables are provided), the igraph library for C++ has to be installed. The makefile has the default path and flags from this library; Then, the user just has to type 'make' in the terminal, in the main directory (the directory where the makefile is); <br />
	To run the Python code, the NetworkX library has to be installed; <br />
	It is assumed that all the code will be run from the main directory: to run the C++ executables files, the command './Executables/<exec_name>' has to be issued in the terminal; <br />
	The Python files should also be analogously run from this directory: 'python3 <folder_that_has_the_file>/<exec_file>.py; This is because all the files written by the ran programs have their paths relative to the main folder. <br />
