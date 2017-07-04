import igraph as ig
import louvain as louvain
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import community

#better with karate_graph() as defined in networkx example.
#erdos renyi don't have true community structure

g = ig.Graph.Read_GML("2017-07-01_Academy_users_100.gml")

# clean nodes in gml file
del g.vs["image"]
del g.vs["file"]
del g.vs["shape"]
del g.vs["type"]
del g.vs["listed"]
del g.vs["ffr"]
del g.vs["lfr"]

# clean edges in gml file
del g.es["weight"]

# graph informations
nodes = g.vcount()
edges = g.ecount()
density = g.density(loops=False)
degree = g.degree()
diameter = g.diameter(directed=True, unconn=True, weights=None)
community_edge_betweenness = g.community_edge_betweenness(directed=True, weights=None)
# community_infomap = g.community_infomap(edge_weights=None, vertex_weights=None, trials=10)
# community_label_propagation = g.community_label_propagation(weights=None, initial=None, fixed=None)
# community_optimal_modularity = g.community_optimal_modularity(weights=None)
# g.modularity(community_infomap, weights=None)
# g.modularity(community_optimal_modularity, weights=None)
assortativity = g.assortativity_degree(directed=True)
# assortativity_nominal = assortativity_nominal(types, directed=True
# authority_score = g.authority_score(weights=None, scale=True, return_eigenvalue=False)
average_path_length = g.average_path_length(directed=True, unconn=True)
# betweenness = g.betweenness(vertices=None, directed=True, cutoff=None, weights=None, nobigint=True)
cliques = g.cliques(min=3)
clusters = g.clusters()
# farthest_points = g.farthest_points(directed=True, unconn=True, weights=None)
g.independent_vertex_sets(min=0, max=0)
bibartite = g.is_bipartite(return_types=False)
connected = g.is_connected(mode=STRONG)
knn = g.knn(vids=None, weights=None)
largest_cliques = g.largest_cliques()
largest_independent_vertex = g.largest_independent_vertex_sets()
max_degree = g.maxdegree(vertices=None, mode=ALL, loops=False)
neighborhood = g.neighborhood(vertices=None, order=1, mode=ALL)
neighborhood_size = g.neighborhood_size(vertices=None, order=1, mode=ALL)
path_length_hist = g.path_length_hist(directed=True)


# change id for louvain
for i in range(len(g.vs)):
    # g.vs[i]["id_old"] = g.vs[i]["id"]
    g.vs[i]["id"] = i

# louvain
part = louvain.find_partition(g, method='Modularity')
part.quality = int(part.quality)
modularity = str(g.modularity(part, weights=None))

# add community to nodes
ids = g.vs["id"]
ids_count = len(ids)

communities = {}

for com_id in range(len(part)):
    com = part[com_id]
    for vertex in com:
        communities[vertex] = com_id

for v in g.vs:
    v["community"] = communities[v["id"]]

# cleaned graph
# print(g)

# g.get_edgelist()
# g.degree(type="in")
# g.degree(type="out")
# g.vs.select(_degree = g.maxdegree())["label"]

# layout
# layout = g.layout_fruchterman_reingold()

# print infos
print('number of nodes: %d' % nodes)
print('number of edges: %d' % edges)
print('density: %d' % density)
print('max degree: %d' % max_degree)
# print('degree: %s' % degree) # find max degree / avg
print('diameter: %d' % diameter)
print('community edge betweenness: %s' % community_edge_betweenness)
print('number of communities: %d' % nbr_commnities)
print('number of degrees: %d' % nbr_degrees)
print('modularity: %s' % modularity)
print('paritition quality: %d' % part.quality)
print('assortativity: %s' % assortativity)
print('average path lenght: %s' % average_path_length)
print('cliques: %s' % cliques)
# print('clusters: %s' % clusters)
# print('farthest_points: %s' % farthest_points)
print('bibartite?: %s' % bibartite)
print('connected?: %s' % connected)
print('knn: %s' % knn)
print('largest cliques: %s' % largest_cliques)
print('largest independent vertices: %s' % largest_independent_vertex)
# print('neighborhood: %s' % neighborhood)
print('neighborhood size: %s' % neighborhood_size)
print('path length: %s' % path_length_hist)


# export new gml
g.save("Academy.gml", format="gml")
