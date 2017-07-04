import igraph as ig
import louvain as louvain
import networkx as nx
import cairo

g = ig.Graph.Read_GML("2017-07-01_Academy_users_100.gml")

# clean nodes in gml file
del g.vs["image"]
del g.vs["shape"]
del g.es["weight"]

g # cleaned graph

# g.degree(type="in")
# g.degree(type="out")
# g.vs.select(_degree = g.maxdegree())["label"]

# layout cairo
layout = g.layout_kamada_kawai()

#louvain
part = louvain.find_partition(G, method='Modularity');

# export new gml

# ig.Graph.write_gml()
