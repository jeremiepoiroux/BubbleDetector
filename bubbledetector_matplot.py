import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import pandas as pd
import json
import requests
from collections import Counter
from statistics import median
import time
import pylab as pl
import pygal
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib import cm
from astropy.convolution import convolve
from astropy.convolution.kernels import Gaussian2DKernel
import scipy.ndimage as sp
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import sphviewer as sph

# open json file

with open("BTW17.json") as json_file:
    s = json.load(json_file)

# coord datasets

xs = []
for i in range(len(s["nodes"])):
    xs.append(s["nodes"][i]["x"])

ys = []
for i in range(len(s["nodes"])):
    ys.append(s["nodes"][i]["y"])

xs_0 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        xs_0.append(s["nodes"][i]["x"])

ys_0 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        ys_0.append(s["nodes"][i]["y"])

xs_1 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        xs_1.append(s["nodes"][i]["x"])

ys_1 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        ys_1.append(s["nodes"][i]["y"])

xs_2 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        xs_2.append(s["nodes"][i]["x"])

ys_2 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        ys_2.append(s["nodes"][i]["y"])

xs_3 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        xs_3.append(s["nodes"][i]["x"])

ys_3 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        ys_3.append(s["nodes"][i]["y"])

xs_4 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        xs_4.append(s["nodes"][i]["x"])

ys_4 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        ys_4.append(s["nodes"][i]["y"])

# ids

ids = []
for i in range(len(s["nodes"])):
    ids.append(s["nodes"][i]["id"])

# communities

community = []
for i in range(len(s["nodes"])):
    community.append(s["nodes"][i]["community"])

# degree total and by community

degree = []
for i in range(len(s["nodes"])):
    degree.append(s["nodes"][i]["degree"])

degree_0 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        degree_0.append(s["nodes"][i]["degree"])

degree_1 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        degree_1.append(s["nodes"][i]["degree"])

degree_2 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        degree_2.append(s["nodes"][i]["degree"])

degree_3 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        degree_3.append(s["nodes"][i]["degree"])

degree_4 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        degree_4.append(s["nodes"][i]["degree"])

# indegree total and by community

indegree = []
for i in range(len(s["nodes"])):
    indegree.append(s["nodes"][i]["indegree"])

indegree_0 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        indegree_0.append(s["nodes"][i]["indegree"])

indegree_1 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        indegree_1.append(s["nodes"][i]["indegree"])

indegree_2 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        indegree_2.append(s["nodes"][i]["indegree"])

indegree_3 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        indegree_3.append(s["nodes"][i]["indegree"])

indegree_4 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        indegree_4.append(s["nodes"][i]["indegree"])


# outdegree total and by community

outdegree = []
for i in range(len(s["nodes"])):
    outdegree.append(s["nodes"][i]["outdegree"])

outdegree_0 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        outdegree_0.append(s["nodes"][i]["outdegree"])

outdegree_1 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        outdegree_1.append(s["nodes"][i]["outdegree"])

outdegree_2 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        outdegree_2.append(s["nodes"][i]["outdegree"])

outdegree_3 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        outdegree_3.append(s["nodes"][i]["outdegree"])

outdegree_4 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        outdegree_4.append(s["nodes"][i]["outdegree"])

# b1 total and by community

b1 = []
for i in range(len(s["nodes"])):
    b1.append(s["nodes"][i]["b1"])

b1_0 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        b1_0.append(s["nodes"][i]["b1"])

b1_1 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        b1_1.append(s["nodes"][i]["b1"])

b1_2 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        b1_2.append(s["nodes"][i]["b1"])

b1_3 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        b1_3.append(s["nodes"][i]["b1"])

b1_4 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        b1_4.append(s["nodes"][i]["b1"])

# b2 total and by community

b2 = []
for i in range(len(s["nodes"])):
    b2.append(s["nodes"][i]["b2"])

b2_0 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        b2_0.append(s["nodes"][i]["b2"])

b2_1 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        b2_1.append(s["nodes"][i]["b2"])

b2_2 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        b2_2.append(s["nodes"][i]["b2"])

b2_3 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        b2_3.append(s["nodes"][i]["b2"])

b2_4 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        b2_4.append(s["nodes"][i]["b2"])

# bubbliness total and by community

bubbliness = []
for i in range(len(s["nodes"])):
    bubbliness.append(s["nodes"][i]["bubbliness"])

bubbliness_0 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        bubbliness_0.append(s["nodes"][i]["bubbliness"])

bubbliness_1 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        bubbliness_1.append(s["nodes"][i]["bubbliness"])

bubbliness_2 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        bubbliness_2.append(s["nodes"][i]["bubbliness"])

bubbliness_3 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        bubbliness_3.append(s["nodes"][i]["bubbliness"])

bubbliness_4 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        bubbliness_4.append(s["nodes"][i]["bubbliness"])

# means

def means(i, list_used):
    l = []
    for j in i:
        if j != -1:
            l.append(j)
    print("mean " + list_used + str(sum(l)/len(l)) + " median " + list_used + str(median(l)))

means(degree, "degree: ")
means(indegree, "indegree: ")
means(outdegree, "outdegree: ")
means(b1, "b1: ")
means(b2, "b2: ")
means(bubbliness, "bubbliness: ")

means(degree_0, "degree: ")
means(indegree_0, "indegree: ")
means(outdegree_0, "outdegree: ")
means(b1_0, "b1: ")
means(b2_0, "b2: ")
means(bubbliness_0, "bubbliness: ")

means(degree_1, "degree: ")
means(indegree_1, "indegree: ")
means(outdegree_1, "outdegree: ")
means(b1_1, "b1: ")
means(b2_1, "b2: ")
means(bubbliness_1, "bubbliness: ")

means(degree_2, "degree: ")
means(indegree_2, "indegree: ")
means(outdegree_2, "outdegree: ")
means(b1_2, "b1: ")
means(b2_2, "b2: ")
means(bubbliness_2, "bubbliness: ")

means(degree_3, "degree: ")
means(indegree_3, "indegree: ")
means(outdegree_3, "outdegree: ")
means(b1_3, "b1: ")
means(b2_3, "b2: ")
means(bubbliness_3, "bubbliness: ")

means(degree_4, "degree: ")
means(indegree_4, "indegree: ")
means(outdegree_4, "outdegree: ")
means(b1_4, "b1: ")
means(b2_4, "b2: ")
means(bubbliness_4, "bubbliness: ")

max(indegree)
max(outdegree)
max(b1)
max(b2)
max(bubbliness)

min(indegree)
min(outdegree)
min(b1)
min(b2)
min(bubbliness)

# scatters

def plot_scatter(col, scale, title, t):
    x = xs
    y = ys
    s = 100
    my_dpi = 96
    plt.figure(figsize=(897/my_dpi, 721/my_dpi), dpi=my_dpi)
    plt.scatter(x, y, alpha=1, s=s, c=col, cmap=scale, edgecolor='black', linewidth='1')
    plt.title('#BTW17 - ' + title + '  - Version du ' + str(time.asctime()))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 897)
    plt.ylim(0, 721)
    plt.autoscale(False)
    plt.gca().invert_yaxis()
    plt.axis('off')
    if t != []:
        cbar = plt.colorbar(ticks=t)
    plt.savefig("BTW17_" + title + '_scatter.png', dpi=200)
    # plt.show()
    # plt.draw()
    plt.close()


plot_scatter(community, "tab10", "Communities", [])
plot_scatter(indegree, "Purples", "Indegree", [min(indegree), int(median(indegree)), max(indegree)])
plot_scatter(outdegree, "Blues", "Outdegree", [min(outdegree), int(median(outdegree)), max(outdegree)])
plot_scatter(b1, "Greens", "b1", [min(b1), int(median(b1)), max(b1)])
plot_scatter(b2, "Oranges", "b2", [min(b2), int(median(b2)), max(b2)])
plot_scatter(bubbliness, "Greys", "Bubbliness", [min(bubbliness), int(median(bubbliness)), max(bubbliness)])

# histograms

def plot_hist(data, colors, title, length):
    plt.figure(figsize=(500/96, 350/96), dpi=96)
    plt.hist(data, color=colors, bins=length)
    plt.title('#BTW17 - Statistics - ' + title + '\n  - Version du ' + str(time.asctime()))
    # plt.xlabel('Value of indegree')
    plt.ylabel('Number of nodes')
    # plt.xlim(0, 897)
    # plt.ylim(0, 721)
    plt.autoscale(False)
    plt.savefig("BTW17_" + title + '_histogram.png', dpi=96)
    # plt.show()
    plt.close()

plot_hist(indegree, "#3F007D", "Indegree whole network", len(set(indegree)))
plot_hist(outdegree, "#07306E", "Outdegree whole network", len(set(outdegree)))
plot_hist(b1, 'green', "b1 whole network", len(set(b1)))
plot_hist(b2, 'orange', "b2 whole network", len(set(b2)))
plot_hist(bubbliness, 'grey', "bubbliness whole network", len(set(bubbliness)))

plot_hist(indegree_0, "#3F007D", "Indegree community 0", len(set(indegree_0)))
plot_hist(outdegree_0, "#07306E", "Outdegree community 0", len(set(outdegree_0)))
plot_hist(b1_0, 'green', "b1 community 0", len(set(b1_0)))
plot_hist(b2_0, 'orange', "b2 community 0", len(set(b2_0)))
plot_hist(bubbliness_0, 'grey', "bubbliness community 0", len(set(bubbliness_0)))

plot_hist(indegree_1, "#3F007D", "Indegree community 1", len(set(indegree_1)))
plot_hist(outdegree_1, "#07306E", "Outdegree community 1", len(set(outdegree_1)))
plot_hist(b1_1, 'green', "b1 community 1", len(set(b1_1)))
plot_hist(b2_1, 'orange', "b2 community 1", len(set(b2_1)))
plot_hist(bubbliness_1, 'grey', "bubbliness community 1", len(set(bubbliness_1)))

plot_hist(indegree_2, "#3F007D", "Indegree community 2", len(set(indegree_2)))
plot_hist(outdegree_2, "#07306E", "Outdegree community 2", len(set(outdegree_2)))
plot_hist(b1_2, 'green', "b1 community 2", len(set(b1_2)))
plot_hist(b2_2, 'orange', "b2 community 2", len(set(b2_2)))
plot_hist(bubbliness_2, 'grey', "bubbliness community 2", len(set(bubbliness_2)))

plot_hist(indegree_3, "#3F007D", "Indegree community 3", len(set(indegree_3)))
plot_hist(outdegree_3, "#07306E", "Outdegree community 3", len(set(outdegree_3)))
plot_hist(b1_3, 'green', "b1 community 3", len(set(b1_3)))
plot_hist(b2_3, 'orange', "b2 community 3", len(set(b2_3)))
plot_hist(bubbliness_3, 'grey', "bubbliness community 3", len(set(bubbliness_3)))

plot_hist(indegree_4, "#3F007D", "Indegree community 4", len(set(indegree_4)))
plot_hist(outdegree_4, "#07306E", "Outdegree community 4", len(set(outdegree_4)))
plot_hist(b1_4, 'green', "b1 community 4", len(set(b1_4)))
plot_hist(b2_4, 'orange', "b2 community 4", len(set(b2_4)))
plot_hist(bubbliness_4, 'grey', "bubbliness community 4", len(set(bubbliness_4)))


#

def heatmap(xx, yy, ww, title):
    x = xx
    y = yy
    my_dpi = 96
    plt.figure(figsize=(500/my_dpi, 500/my_dpi), dpi=my_dpi)
    heatmap, xedges, yedges = np.histogram2d(y, x, bins=200, weights=ww)
    # plt.xlim(0, 897)
    # plt.ylim(0, 721)
    # plt.gca().invert_yaxis()
    # fig, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.imshow(heatmap, interpolation='none')
    # ax2.imshow(convolve(heatmap, Gaussian2DKernel(stddev=10)), interpolation='none')
    plt.imshow(convolve(heatmap, Gaussian2DKernel(stddev=15)), interpolation='none')
    plt.title('#BTW17 - ' + title + '  - Version du ' + str(time.asctime()))
    plt.axis('off')
    plt.autoscale(False)
    # plt.colorbar()
    plt.savefig("BTW17_" + title + '_heatmap.png', dpi=200)
    plt.show()

heatmap(xs, ys, b1, "b1 network")
heatmap(xs_0, ys_0, b1_0, "b1 community0")
heatmap(xs_1, ys_1, b1_1, "b1 community1")
heatmap(xs_2, ys_2, b1_2, "b1 community2")
heatmap(xs_3, ys_3, b1_3, "b1 community3")
heatmap(xs_4, ys_4, b1_4, "b1 community4")

heatmap(xs, ys, b2, "b2_network")
heatmap(xs_0, ys_0, b2_0, "b2 community0")
heatmap(xs_1, ys_1, b2_1, "b2 community1")
heatmap(xs_2, ys_2, b2_2, "b2 community2")
heatmap(xs_3, ys_3, b2_3, "b2 community3")
heatmap(xs_4, ys_4, b2_4, "b2 community4")

heatmap(xs, ys, bubbliness, "bubbliness")
heatmap(xs_0, ys_0, bubbliness_0, "bubbliness community0")
heatmap(xs_1, ys_1, bubbliness_1, "bubbliness community1")
heatmap(xs_2, ys_2, bubbliness_2, "bubbliness community2")
heatmap(xs_3, ys_3, bubbliness_3, "bubbliness community3")
heatmap(xs_4, ys_4, bubbliness_4, "bubbliness community4")

###