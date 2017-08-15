import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import requests
from collections import Counter

with open("BTW17.json") as json_file:
    s = json.load(json_file)

for i in range(len(s["nodes"])):
    if s["nodes"][i]["b1"] == 0:
        print(s["nodes"][i]["b1"])

x = []
for i in range(len(s["nodes"])):
    x.append(s["nodes"][i]["bubbliness"])

z = []
for i in range(len(s["nodes"])):
    z.append(s["nodes"][i]["b1"] / s["nodes"][i]["b2"])

z1 = []
for i in range(len(s["nodes"])):
    z1.append(s["nodes"][i]["b2"] - s["nodes"][i]["b1"])

z1 = []
for i in range(len(s["nodes"])):
    z1.append(s["nodes"][i]["b2"] - s["nodes"][i]["b1"])

# Create data
# N = 6
# x = [205,252,335,336,579,292]
# y = [-55,-82,-97,-127,-427,-670]
# colors = (0,0,0)
# my_dpi = 96
# area = np.pi*3


def plot_hist(data):
    plt.hist(data)
    plt.show()

plot_hist(x)
plot_hist(z)
plot_hist(z1)


# Plot
# plt.figure(figsize=(897/my_dpi, 721/my_dpi), dpi=my_dpi)
# plt.scatter(x, y, c=colors)
# plt.title('Scatter plot pythonspot.com')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xlim(0, 897)
# plt.ylim(-721, 0)
# plt.autoscale(False)

def stats(c):
    co = []
    for i in range(len(s["nodes"])):
        if s["nodes"][i]["community"] == c:
            co.append(s["nodes"][i]["b2"])
    print(sum(co)/len(co))

stats(0)
stats(1)
stats(2)
stats(3)
stats(4)

# count edges from and to communities

df = pd.read_csv("BTW17_2_2017-07-20_users.gml_limited.gml_def.gml_edges.csv", error_bad_lines=False)

community = []
for i in df.index:
    # print(i)
    community.append((df.in_community[i], df.out_community[i]))

community_count = []
for i in community:
    if i[0] == 4:
        # print(i[1])
        community_count.append(i[1])

Counter(community_count)
len(community_count)
