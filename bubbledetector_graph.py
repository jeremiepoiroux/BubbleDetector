import igraph as ig
import louvain as louvain
import numpy as np
import math
import community
import codecs
import collections
import json
import csv
import pandas as pd
# import pandas as pd
# import networkx as nx
# import matplotlib.pyplot as plt

# read gml file
gml_file = input ("Which GML file (with .gml)?: ")
g = ig.Graph.Read_GML(gml_file)

len(g.vs)

# clean nodes in gml file
try:
    del g.vs["image"]
except:
    KeyError
# del g.vs["image"]
del g.vs["file"]
del g.vs["shape"]
del g.vs["type"]
del g.vs["listed"]
del g.vs["ffr"]
del g.vs["lfr"]

# clean edges in gml file
try:
    del g.es["weight"]
except:
    KeyError

# keep only connected nodes
node_degree = g.degree(mode=3)

# number of direct out degree to nodes
for i in range(len(g.vs)):
    g.vs[i]["degree"] = node_degree[i]

to_delete = []
for i in range(len(g.vs)):
    if g.vs[i]["degree"] == 0:
        to_delete.append(i)
g.delete_vertices(to_delete)


# in degree
node_in_degree = g.degree(mode=2)
for i in range(len(g.vs)):
    g.vs[i]["in_degree"] = node_in_degree[i]


# out degree
node_out_degree = g.degree(mode=1)
for i in range(len(g.vs)):
    g.vs[i]["out_degree"] = node_out_degree[i]

# add closeness centrality to nodes
# for i in range(len(g.vs)):
    # g.vs[i]["centrality"] = closeness[i]

# change id for louvain
for i in range(len(g.vs)):
    # g.vs[i]["id_old"] = g.vs[i]["id"]
    g.vs[i]["id"] = i

# louvain
part = louvain.find_partition(g, method='Modularity')
part.quality = int(part.quality)
modularity = str(g.modularity(part, weights=None))
nbr_communities = len(part)

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

print(part)
# part_delete = input ("How many nodes min in communities to keep?: ")

# to_delete_com = []
# for p in part:
    # if len(p) < int(part_delete):
        # for v in p:
            # to_delete_com.append(v)
# g.delete_vertices(to_delete_com)

# bubbliness
# out links inside community 1st circle
# out links outside community 1st circle

# /!\ ISSUE
# for i in range(len(g.vs)):
    # print(g.neighbors(i, mode=1))

# graph informations
nodes = g.vcount()
edges = g.ecount()
node_in_degree = g.degree(mode=2)
node_out_degree = g.degree(mode=1)
density = g.density(loops=False)
max_in_degree = g.maxdegree(vertices=None, mode=2, loops=False)
max_out_degree = g.maxdegree(vertices=None, mode=1, loops=False)
diameter = g.diameter(directed=True, unconn=True, weights=None)
assortativity = g.assortativity_degree(directed=True)
average_path_length = g.average_path_length(directed=True, unconn=True)
bibartite = g.is_bipartite(return_types=False)
connected = g.is_connected()
closeness = g.closeness(vertices=None, mode=3, cutoff=None, weights=None, normalized=True)
dya = g.dyad_census()
# community_edge_betweenness = g.community_edge_betweenness(directed=True, weights=None)
# community_infomap = g.community_infomap(edge_weights=None, vertex_weights=None, trials=10)
# community_label_propagation = g.community_label_propagation(weights=None, initial=None, fixed=None)
# community_optimal_modularity = g.community_optimal_modularity(weights=None)
# g.modularity(community_infomap, weights=None)
# g.modularity(community_optimal_modularity, weights=None)
# assortativity_nominal = assortativity_nominal(types, directed=True
# authority_score = g.authority_score(weights=None, scale=True, return_eigenvalue=False)
# betweenness = g.betweenness(vertices=None, directed=True, cutoff=None, weights=None, nobigint=True)
# clusters = g.clusters()
# farthest_points = g.farthest_points(directed=True, unconn=True, weights=None)
# g.independent_vertex_sets(min=0, max=0)
# knn = g.knn(vids=None, weights=None)
# largest_cliques = g.largest_cliques()
# largest_independent_vertex = g.largest_independent_vertex_sets()
# neighborhood = g.neighborhood(vertices=None, order=1, mode=3)
# neighborhood_size = g.neighborhood_size(vertices=None, order=1, mode=3)
# path_length_hist = g.path_length_hist(directed=True)

# print infos to file
with codecs.open(gml_file + '.txt', 'w', 'utf-8') as tf:
    tf.write("---'" + gml_file + "--- \n \n")
    tf.write("-- General Informations -- \n")
    tf.write("number of nodes: %d \n" % nodes)
    tf.write("number of edges: %d \n" % edges)
    tf.write("density: %s \n" % str(density))
    tf.write("max in degree: %d \n" % max_in_degree)
    tf.write("max out degree: %d \n" % max_out_degree)
    tf.write("diameter: %d \n" % diameter)
    tf.write("number of communities: %d \n" % nbr_communities)
    tf.write("modularity: %s \n" % modularity)
    tf.write("partition quality: %d \n" % part.quality)
    tf.write("assortativity: %s \n" % str(assortativity))
    tf.write("average path length: %d \n" % average_path_length)
    tf.write("bibartite?: %d \n" % bibartite)
    tf.write("connected?: %d \n" % connected)
    tf.write("\n -- Communities informations -- \n")

    # tf.write("clusters: %s \n" % str(clusters))
    # tf.write("community edge betweenness: %s \n" % str(community_edge_betweenness))
    # tf.write("knn: %s \n" % str(knn))
    # tf.write("neighborhood size: %s \n" % n_lenght)
    # tf.write("path length: %s \n" % str(path_length_hist))
    # tf.write("\n")
    # tf.write("-- Nodes informations -- \n")
    # for i in range(len(g.vs)):
        # tf.write("node " + str(i) + ": clos. centr.: " + str(closeness[i]) + ": nb in degree : " + str(node_in_degree[i]) + ": nb out degree : " + str(node_out_degree[i]) + " \n")

# change id for neighborhood
for i in range(len(g.vs)):
    # g.vs[i]["id_old"] = g.vs[i]["id"]
    g.vs[i]["id"] = i

# print(g.vs["id"])
# for i in range(len(g.vs)):
    # print(g.vs[i]["label"])


# for i in range(len(g.vs)):
    # this_node_follows = g.neighborhood(i, mode="out", order=1)
    # print(this_node_follows)

def out_edges(order):
    for i in range(len(g.vs)):
        this_node_follows = g.neighborhood(i, mode="out", order=order)
        this_node_follows = this_node_follows[1:]
        this_node_follows = set(this_node_follows)
        for o in range(order - 1, 0, -1):
            this_node_follows = this_node_follows.difference(set(g.neighborhood(i, mode="out", order=o)))
        community = g.vs[i]["community"]
        out_inside = []
        out_outside = []
        this_node_follows_communities = set()
        for node in this_node_follows:
            this_node_follows_communities.add(g.vs[node]["community"])
            if node not in part[community]:
                out_outside.append(node)
            else:
                out_inside.append(node)
        g.vs[i]["out_inside_%s" % order] = json.dumps(out_inside, separators=(',',':'))
        g.vs[i]["out_outside_%s" % order] = json.dumps(out_outside, separators=(',',':'))
        # g.vs[i]["communities_ratio_%s" % order] = float(len(this_node_follows_communities) + 1) / float(len(this_node_follows) + 1) #normalization?
        len_out_inside = float(len(out_inside))
        len_out_outside = float(len(out_outside))
        g.vs[i]["outgoing_links_inside_community_at_d_%s" % order] = len_out_inside
        g.vs[i]["outgoing_links_outside_community_at_d_%s" % order] = len_out_outside

        if len_out_outside + len_out_inside != 0:
            ratio = len_out_inside / (len_out_outside + len_out_inside)
        else:
            ratio = -1.0
        g.vs[i]["outinside_%s_DIVoutdegree_ratio" % order] = float(ratio) #normalization?
        # g.vs[i]["outinside_%s_DIVoutdegree_discount" % order] = (float(ratio) * float(1/(order**2))) #normalization?

out_edges(1)
out_edges(2)
# out_edges(3)

# for i in range(len(g.vs)):
    # print(g.vs[i]["out_inside_1"])


community = []
for i in range(len(g.vs)):
    com = g.vs[i]["community"]
    community.append(com)
len_c = len(set(community))

for i in range(len(g.vs)):
    if g.vs[i]["outinside_1_DIVoutdegree_ratio"] == -1.0:
        g.vs[i]["bubbliness"] = -1.0
        g.vs[i]["bubbliness_viz"] = -1.0
    elif g.vs[i]["outinside_2_DIVoutdegree_ratio"] == -1.0:
        g.vs[i]["bubbliness"] = -1.0
        g.vs[i]["bubbliness_viz"] = -1.0
    else:
        g.vs[i]["bubbliness_viz"] = ((g.vs[i]["outinside_2_DIVoutdegree_ratio"]) - (g.vs[i]["outinside_1_DIVoutdegree_ratio"]) + 1)/2
        g.vs[i]["bubbliness"] = (g.vs[i]["outinside_2_DIVoutdegree_ratio"]) - (g.vs[i]["outinside_1_DIVoutdegree_ratio"])

# for i in range(len(g.vs)):
    # g.vs[i]["ratio_outgoing_links_inside_community_mean"] = (g.vs[i]["outinside_1_DIVoutdegree_ratio"] + g.vs[i]["outinside_2_DIVoutdegree_ratio"] + g.vs[i]["outinside_3_DIVoutdegree_ratio"]) / 3

# for i in range(len(g.vs)):
    # g.vs[i]["ratio_outgoing_links_inside_community_discount"] = (g.vs[i]["outinside_1_DIVoutdegree_discount"] + g.vs[i]["outinside_2_DIVoutdegree_discount"] + g.vs[i]["outinside_3_DIVoutdegree_discount"]) / 3

# DIJKSTRA’S ALGORITHM
# for i in range(len(g.vs)):
    # spd = g.shortest_paths_dijkstra(source=i, target=None, weights=None, mode=1)
    # spd = spd[0]
    # spd = [item for item in enumerate(spd) if 0 < item[1] < 4]
    # spd_str = json.dumps(spd, separators=(',',':'))
    # g.vs[i]["dijkstra"] = spd_str



# export new gml
g.save(gml_file + "_def.gml", format="gml")

# communities informations
'''
def l():
    return [x for x in range(len_c)]
part_length = l()

def com_bub(comm):
    community_bubbliness_d1_list = []
    community_bubbliness_d1_list_discount = []
    for i in range(len(g.vs)):
        if g.vs[i]["community"] == comm:
            community_bubbliness_d1_list.append(g.vs[i]["outinside_1_DIVoutdegree_ratio"])
            community_bubbliness_d1_list_discount.append(g.vs[i]["outinside_1_DIVoutdegree_discount"])

    community_bubbliness_d1 = sum(community_bubbliness_d1_list)/len(community_bubbliness_d1_list)
    community_bubbliness_d1_discount = sum(community_bubbliness_d1_list_discount)/len(community_bubbliness_d1_list_discount)
    # print("community %d bubb:" + str(community_bubbliness_d1) % comm)
    with codecs.open(gml_file + '.txt', 'a', 'utf-8') as tf:
        tf.write("community " + str(comm) + " bubbliness at d=1): " + str(community_bubbliness_d1) + "\n ")
        tf.write("community " + str(comm) + " bubbliness discount at d=1): " + str(community_bubbliness_d1_discount) + "\n ")

for l in part_length:
    com_bub(l)

def com_bub(comm):
    community_bubbliness_d2_list = []
    community_bubbliness_d2_list_discount = []
    for i in range(len(g.vs)):
        if g.vs[i]["community"] == comm:
            community_bubbliness_d2_list.append(g.vs[i]["outinside_2_DIVoutdegree_ratio"])
            community_bubbliness_d2_list_discount.append(g.vs[i]["outinside_2_DIVoutdegree_discount"])

    community_bubbliness_d2 = sum(community_bubbliness_d2_list)/len(community_bubbliness_d2_list)
    community_bubbliness_d2_discount = sum(community_bubbliness_d2_list_discount)/len(community_bubbliness_d2_list_discount)
    # print("community %d bubb:" + str(community_bubbliness_d1) % comm)
    with codecs.open(gml_file + '.txt', 'a', 'utf-8') as tf:
        tf.write("community " + str(comm) + " bubbliness at d=2): " + str(community_bubbliness_d2) + "\n ")
        tf.write("community " + str(comm) + " bubbliness discount at d=2): " + str(community_bubbliness_d2_discount) + "\n ")


for l in part_length:
    com_bub(l)

def com_bub(comm):
    community_bubbliness_d3_list = []
    community_bubbliness_d3_list_discount = []
    for i in range(len(g.vs)):
        if g.vs[i]["community"] == comm:
            community_bubbliness_d3_list.append(g.vs[i]["outinside_3_DIVoutdegree_ratio"])
            community_bubbliness_d3_list_discount.append(g.vs[i]["outinside_3_DIVoutdegree_discount"])

    community_bubbliness_d3 = sum(community_bubbliness_d3_list)/len(community_bubbliness_d3_list)
    community_bubbliness_d3_discount = sum(community_bubbliness_d3_list_discount)/len(community_bubbliness_d3_list_discount)
    # print("community %d bubb:" + str(community_bubbliness_d1) % comm)
    with codecs.open(gml_file + '.txt', 'a', 'utf-8') as tf:
        tf.write("community " + str(comm) + " bubbliness at d=3): " + str(community_bubbliness_d3) + "\n ")
        tf.write("community " + str(comm) + " bubbliness discount at d=3): " + str(community_bubbliness_d3_discount) + "\n ")

for l in part_length:
    com_bub(l)

'''

# cleaned graph
# print(g)
# print(g.get_edgelist())
# g.degree(type="in")
# g.degree(type="out")
# g.vs.select(_degree = g.maxdegree())["label"]
