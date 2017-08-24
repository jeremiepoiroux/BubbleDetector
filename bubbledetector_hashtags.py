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
from operator import is_not
from functools import partial

g = ig.Graph.Read_GML("BTW17_2_2017-07-20_users.gml_limited.gml_def.gml")
t = pd.read_csv("BTW17_2_2017-07-20.csv", error_bad_lines=False)

gml = []
for i in range(len(g.vs)):
    gml.append((g.vs[i]["label"], g.vs[i]["community"]))

####
df_list = t.values.tolist()

list_of_hashtags = []
for r in gml:
    if r[1] == 1:
        # print(r[0])
        for d in df_list:
            if r[0] in d[4].lower():
                list_of_hashtags.append(d[8])
                list_of_hashtags.append(d[9])
                list_of_hashtags.append(d[10])

len(list_of_hashtags)

f = partial(is_not, np.nan)
x = list_of_hashtags
list_of_hashtags_v2 = list(filter(f, x))

list_of_hashtags_v3 = []
for i in list_of_hashtags_v2:
    list_of_hashtags_v3.append(i.lower())

list_of_hashtags_count = Counter(list_of_hashtags_v3)
# list_of_hashtags_count

sorted_hashtags = sorted(list_of_hashtags_count.items())
sorted_hashtags_2 = sorted(sorted_hashtags, key=lambda x: x[1])
sorted_hashtags_2[-10:]
