import osmnx as ox
import networkx as nx



def create_map(location,dist,color):
    base_map = ox.graph_from_point(location, dist = dist, simplify=True)
    ox.plot_graph(base_map, figsize= (10,8),bgcolor= "#00000000", node_size=5, edge_color=color)