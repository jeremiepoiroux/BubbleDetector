import igraph as ig
import codecs
import csv

gml_file = input ("Which GML file (with .gml)?: ")
g = ig.Graph.Read_GML(gml_file)

for i in range(len(g.vs)):
    idd = int(g.vs[i]["id"])
    inin1 = int(g.vs[i]["outgoinglinksinsidecommunityatd1"])
    inout1 = int(g.vs[i]["outgoinglinksoutsidecommunityatd1"])
    inin2 = int(g.vs[i]["outgoinglinksinsidecommunityatd2"])
    inout2 = int(g.vs[i]["outgoinglinksoutsidecommunityatd2"])
    inin3 = int(g.vs[i]["outgoinglinksinsidecommunityatd3"])
    inout3 = int(g.vs[i]["outgoinglinksoutsidecommunityatd3"])
    dijkstra = g.vs[i]["dijkstra"]
    with codecs.open(gml_file + '_camille.csv', 'a', 'utf-8') as csvfile:
        tf = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        tf.writerow([idd, inin1, inout1, inin2, inout2, inin3, inout3, dijkstra])
