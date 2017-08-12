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


# TO DO AGAIN
def links_to_communities(c):
    links_from_community = []
    for i in range(len(s["nodes"])):
        if s["nodes"][i]["community"] == c:
            j = s["nodes"][i]["list_of_friends_outside_community_at_distance_1"]
            k = s["nodes"][i]["list_of_friends_inside_community_at_distance_1"]
            l = json.loads(j)
            m = json.loads(m)
            for ll in l:
                links_from_community.append(s["nodes"][ll]["community"])
    print(Counter(links_from_community))

links_to_communities(0)
links_to_communities(1)
links_to_communities(2)
links_to_communities(3)
links_to_communities(4)
