import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import requests
from collections import Counter

with open("feminismus.json") as json_file:
    s = json.load(json_file)

# count edges from and to communities

df = pd.read_csv("feminismus_2017-07-09_users.gml_limited.gml_def.gml_edges.csv", error_bad_lines=False)

community = []
for i in df.index:
    # print(i)
    community.append((df.in_community[i], df.out_community[i]))

community_count = []
for i in community:
    if i[0] == 5:
        # print(i[1])
        community_count.append(i[1])

Counter(community_count)
len(community_count)
