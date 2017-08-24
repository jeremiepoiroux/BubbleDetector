import igraph as ig
import codecs
import csv
import pandas as pd
import json
import numpy

# read definitive gml file
gml_file = input ("Which GML file (with _def.gml)?: ")
g = ig.Graph.Read_GML(gml_file)

# read x,y csv
# csv_file = input ("Which csv file (with _xy.csv)?: ")
# xy = pd.read_csv(csv_file, error_bad_lines=False)
# xy = xy.sort_values('id', ascending=True)
# xy = xy.reset_index(drop=True)
# print(xy)
# xy.to_csv(csv_file + "_new.csv", index=True)
# xy.iloc[80]
# xy.loc[80]
# create pandas dataframe with nodes
nodes = pd.DataFrame()

# populate dataframe
nodes['id'] = [int(v['id']) for v in g.vs]
# nodes['user_id'] = [v['userid'] for v in g.vs]
nodes['label'] = [v['label'] for v in g.vs]
nodes['total_of_statuses'] = [int(v['statuses']) for v in g.vs]
nodes['total_of_friends'] = [int(v['friends']) for v in g.vs]
nodes['total_of_followers'] = [int(v['followers']) for v in g.vs]

nodes['degree'] = [int(v['degree']) for v in g.vs]
nodes['indegree'] = [int(v['indegree']) for v in g.vs]
nodes['outdegree'] = [int(v['outdegree']) for v in g.vs]
nodes['community'] = [int(v['community']) for v in g.vs]

nodes['list_of_friends_inside_community_at_distance_1'] = [v['outinside1'] for v in g.vs]
nodes['list_of_friends_outside_community_at_distance_1'] = [v['outoutside1'] for v in g.vs]
nodes['links_inside_community_at_distance_1'] = [int(v['outgoinglinksinsidecommunityatd1']) for v in g.vs]
nodes['links_outside_community_at_distance_1'] = [int(v['outgoinglinksoutsidecommunityatd1']) for v in g.vs]
nodes['b1'] = [v['outinside1DIVoutdegreeratio'] for v in g.vs]
# nodes['out_inside_1_DIV_outdegree_discount'] = [v['outinside1DIVoutdegreediscount'] for v in g.vs]

nodes['list_of_friends_inside_community_at_distance_2'] = [v['outinside2'] for v in g.vs]
nodes['list_of_friends_outside_community_at_distance_2'] = [v['outoutside2'] for v in g.vs]
nodes['links_inside_community_at_distance_2'] = [int(v['outgoinglinksinsidecommunityatd2']) for v in g.vs]
nodes['links_outside_community_at_distance_2'] = [int(v['outgoinglinksoutsidecommunityatd2']) for v in g.vs]
nodes['b2'] = [v['outinside2DIVoutdegreeratio'] for v in g.vs]

nodes['bubbliness'] = [v['bubbliness'] for v in g.vs]
# nodes['out_inside_2_DIV_outdegree_discount'] = [v['outinside2DIVoutdegreediscount'] for v in g.vs]

# nodes['outgoing_links_inside_community_at_d3'] = [int(v['outgoinglinksinsidecommunityatd3']) for v in g.vs]
# nodes['outgoing_links_outside_community_at_d3'] = [int(v['outgoinglinksoutsidecommunityatd3']) for v in g.vs]
# nodes['out_inside_3_DIV_outdegree_ratio'] = [v['outinside3DIVoutdegreeratio'] for v in g.vs]
# nodes['out_inside_3_DIV_outdegree_discount'] = [v['outinside3DIVoutdegreediscount'] for v in g.vs]

# nodes['ratio_outgoing_links_inside_community_mean'] = [v['ratiooutgoinglinksinsidecommunitymean'] for v in g.vs]
# nodes['ratio_outgoing_links_inside_community_discount'] = [v['ratiooutgoinglinksinsidecommunitydiscount'] for v in g.vs]

# for i in xy.id:
    # nodes['x'] = xy.x

# for i in xy.id:
    # nodes['y'] = xy.y

# export dataframe to csv
nodes.to_csv(gml_file + '_nodes.csv', index=False)

# create pandas dataframe with edges
edges = pd.DataFrame()
edges_kumu = pd.DataFrame()

g.es["source"] = [e.source for e in g.es]
g.es["target"] = [e.target for e in g.es]

# g.es["sme"] = [e.source for e in g.es]

edges_kumu['from'] = g.es["source"]
edges_kumu['to'] = g.es["target"]

edges['source'] = g.es["source"]
edges['target'] = g.es["target"]

out_community = []
for i in range(len(g.vs)):
    b = g.vs[i]["id"]
    c = int(g.vs[i]["community"])
    # print(b)
    # print(c)
    for e in g.es["source"]:
        if e == b:
            # print(c)
            out_community.append(c)

edges["out_community"] = out_community

in_community = []
for e in g.es['target']:
     in_community.append(int(g.vs[e]["community"]))
edges["in_community"] = in_community

# export dataframe to csv

edges.to_csv(gml_file + '_edges.csv', index=False)
edges_kumu.to_csv(gml_file + '_edges_kumu.csv', index=False)

# export to JSON
nodes_json = nodes.to_json(orient='records', double_precision=2)
edges_json = edges.to_json(orient='records', double_precision=2)

print("{\"nodes\":")
print(nodes_json)
print(",\"links\":")
print(edges_json + "}")

with codecs.open("feminismus.json", 'w', 'utf-8') as tf:
    tf.write("{\"nodes\":")
    tf.write(nodes_json)
    tf.write(",\"links\":")
    tf.write(edges_json + "}")

'''# COLOR SCALE
nodes_list = []
for n in nodes['bubbliness']:
    if n != -1.0:
        nodes_list.append(n)

nodes_list.sort()
len(nodes_list)
mean = sum(nodes_list) / len(nodes_list)
mean
numpy.percentile(nodes_list, 75, interpolation='higher')
numpy.percentile(nodes_list, 25, interpolation='lower')
numpy.percentile(nodes_list, 50, interpolation='lower')
numpy.median(nodes_list)

nodes_list
'''
