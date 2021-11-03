import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

model = 0
while True:
	try:
		model = int(input("Choose model (0 - BA; 1 - DMS; 2 - Small Example): "))       
	except ValueError:
		print("Please enter 0, 1 or 2:")
		continue
	else:
		if model >= 0 or model <= 2:
			break
		else:
			continue

criteria = 0
while True:
	try:
		criteria = int(input("Choose criteria (0, 1, 2 or 3): "))       
	except ValueError:
		print("Please enter an integer between 0 and 3:")
		continue
	else:
		if criteria >= 0 and criteria <= 3:
			break
		else:
			continue

if model == 0:
	G = nx.read_gml("Animation/Graphs/ba.gml", None)
	file_name = "Animation/Data/ba_%i.txt" % criteria
elif model == 1:
	G = nx.read_gml("Animation/Graphs/dms.gml", None)
	file_name = "Animation/Data/dms_%i.txt" % criteria
else:
	G = nx.read_gml("Animation/Graphs/small.gml", None)
	file_name = "Animation/Data/small_%i.txt" % criteria

edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Network graph made with Python',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()