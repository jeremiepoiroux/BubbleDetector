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
from math import pi
# import sphviewer as sph

# open json file

with open("BTW17.json") as json_file:
    s = json.load(json_file)

# s
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

Counter(community)

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




bubbliness_viz = []
for i in range(len(s["nodes"])):
    bubbliness_viz.append(s["nodes"][i]["bubbliness_viz"])

bubbliness_0_viz = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        bubbliness_0_viz.append(s["nodes"][i]["bubbliness_viz"])

bubbliness_1_viz = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        bubbliness_1_viz.append(s["nodes"][i]["bubbliness_viz"])

bubbliness_2_viz = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        bubbliness_2_viz.append(s["nodes"][i]["bubbliness_viz"])

bubbliness_3_viz = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        bubbliness_3_viz.append(s["nodes"][i]["bubbliness_viz"])

bubbliness_4_viz = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        bubbliness_4_viz.append(s["nodes"][i]["bubbliness_viz"])

# number of times people were retweeted

retweeted_counter = Counter({'afd_hd': 2,
         'afdduesseldorf': 4,
         'andreasandy3131': 5,
         'btwahltrend': 1,
         'espendillerm': 36,
         'joeygerlach': 15,
         'politik_zz': 1,
         'v_palme': 3,
         'xnews24': 2})

retweeted_list = sorted(retweeted_counter.items())

# for r in retweeted_list:
    # print(r[0])
    # print(s["nodes"][r[1]]["label"])

retweeted_list_final = []

for i in range(len(s["nodes"])):
    j = s['nodes'][i]['label']
    for r in retweeted_list:
        if j == r[0]:
            retweeted_list_final.append((s['nodes'][i]['id'], s['nodes'][i]['label'], s['nodes'][i]['community'], r[1]))
            # print(r[1])

# retweeted_list_final

for i in range(len(s["nodes"])):
    s['nodes'][i]['times_retweeted'] = 0

for i in range(len(s["nodes"])):
    for r in retweeted_list_final:
    # print(s['nodes'][i]['id'])
        if s['nodes'][i]['id'] == r[0]:
            # print(r[0], r[3])
            s['nodes'][i]['times_retweeted'] = r[3]

times_retweeted = []
for i in range(len(s["nodes"])):
    if s['nodes'][i]['times_retweeted']:
        times_retweeted.append(s['nodes'][i]['times_retweeted'])
    else:
        times_retweeted.append(0)

were_retweeted = []
for i in range(len(s["nodes"])):
    were_retweeted.append(s["nodes"][i]["times_retweeted"])

were_retweeted_0 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        were_retweeted_0.append(s["nodes"][i]["times_retweeted"])

were_retweeted_1 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        were_retweeted_1.append(s["nodes"][i]["times_retweeted"])

were_retweeted_2 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        were_retweeted_2.append(s["nodes"][i]["times_retweeted"])

were_retweeted_3 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        were_retweeted_3.append(s["nodes"][i]["times_retweeted"])

were_retweeted_4 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        were_retweeted_4.append(s["nodes"][i]["times_retweeted"])


# for i in range(len(s["nodes"])):
    # if s["nodes"][i]["community"] == 4:
        # print(s["nodes"][i]["times_retweet"])

# number of times people retweet

retweet_counter = Counter({'1netzreport': 1,
         'afd_hd': 1,
         'afd_support': 1,
         'afdduesseldorf': 1,
         'andreasandy3131': 4,
         'bernd471': 4,
         'chungun88': 1,
         'darkynanmp': 1,
         'derliuhvan': 1,
         'derpatriot444': 1,
         'erhardtresch': 1,
         'eusebius217': 1,
         'f_von_steiner': 1,
         'gerrywinkl': 2,
         'gomander2': 3,
         'grandel1': 1,
         'heischonin': 1,
         'hevellia64': 1,
         'iamarealrealist': 1,
         'isidormeyer1': 1,
         'kauflogos': 1,
         'leon_dnebach': 1,
         'loose_afd': 1,
         'magna_est': 1,
         'megatwingo': 1,
         'merteo1': 1,
         'michistelle': 1,
         'mundaufmachen': 1,
         'ollimike': 2,
         'parteilos59': 1,
         'paulahasi13': 2,
         'paulplotzer': 2,
         'peterbeta69': 1,
         'peterpa34083139': 2,
         'plingl': 1,
         'raluka19830803': 1,
         'regionalreport': 1,
         's_muenzenmaier': 1,
         'tartilleri': 3,
         'thomasboro': 2,
         'thomasgbauer': 1,
         'thomasraue': 1,
         'tonkhonkey': 1,
         'traudichde': 5,
         'ueberflug': 1,
         'uwebecher': 1,
         'wicked777223': 1,
         'zufallszahl': 3})

retweet_list = sorted(retweet_counter.items())

# for r in retweeted_list:
    # print(r[0])
    # print(s["nodes"][r[1]]["label"])

retweet_list_final = []

for i in range(len(s["nodes"])):
    j = s['nodes'][i]['label']
    for r in retweet_list:
        if j == r[0]:
            retweet_list_final.append((s['nodes'][i]['id'], s['nodes'][i]['label'], s['nodes'][i]['community'], r[1]))
            # print(r[1])

for i in range(len(s["nodes"])):
    s['nodes'][i]['times_retweet'] = 0

for i in range(len(s["nodes"])):
    for r in retweet_list_final:
    # print(s['nodes'][i]['id'])
        if s['nodes'][i]['id'] == r[0]:
            # print(r[0], r[3])
            s['nodes'][i]['times_retweet'] = r[3]

# s["nodes"][128]

times_retweet = []
for i in range(len(s["nodes"])):
    if s['nodes'][i]['times_retweet']:
        times_retweet.append(s['nodes'][i]['times_retweet'])
    else:
        times_retweet.append(0)
# times_retweet

# RT by communities
# Retweeted
retweeted_list_final_com = []
for r in retweeted_list_final:
    retweeted_list_final_com.append(r[2])

Counter(retweeted_list_final_com)

# Retweeters
retweet_list_final_com = []
for r in retweet_list_final:
    retweet_list_final_com.append(r[2])

Counter(retweet_list_final_com)

have_retweeted = []
for i in range(len(s["nodes"])):
    have_retweeted.append(s["nodes"][i]["times_retweet"])

have_retweeted_0 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 0:
        have_retweeted_0.append(s["nodes"][i]["times_retweet"])

have_retweeted_1 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 1:
        have_retweeted_1.append(s["nodes"][i]["times_retweet"])

have_retweeted_2 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 2:
        have_retweeted_2.append(s["nodes"][i]["times_retweet"])

have_retweeted_3 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 3:
        have_retweeted_3.append(s["nodes"][i]["times_retweet"])

have_retweeted_4 = []
for i in range(len(s["nodes"])):
    if s["nodes"][i]["community"] == 4:
        have_retweeted_4.append(s["nodes"][i]["times_retweet"])

tweets = [('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:02:17 +0000 2017',
  'afd_support'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:50:44 +0000 2017',
  'megatwingo'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:31:49 +0000 2017',
  'derpatriot444'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 17:40:24 +0000 2017',
  'zufallszahl'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:33:49 +0000 2017',
  's_muenzenmaier'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 13:20:20 +0000 2017',
  'afd_hd'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 15:23:38 +0000 2017',
  'thomasraue'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:51:54 +0000 2017',
  'raluka19830803'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 13:15:59 +0000 2017',
  'traudichde'),
 ('rt @espendillerm: @stephanmalzkorn brd: nur auf länderebene. wir wollen volksentscheide auch im bund! #afd #btw17 #traudichdeutschland',
  'thu jul 20 21:06:10 +0000 2017',
  'traudichde'),
 ('rt @espendillerm: @guldnerlars und wir möchten es so haben wie in der schweiz! volksentscheide auf bundesebene #traudichdeutschland #afd #b…',
  'thu jul 20 21:17:08 +0000 2017',
  'traudichde'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 13:12:43 +0000 2017',
  'wicked777223'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 16:15:11 +0000 2017',
  'thomasgbauer'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 13:06:46 +0000 2017',
  'gomander2'),
 ('rt @jochen_haug: sehr anschaulich von meinem (hoffentlich) zukünftigen fraktionskollegen im #bundestag, @espendillerm! #btw17 #afd… ',
  'thu jul 20 13:19:58 +0000 2017',
  'gomander2'),
 ('rt @espendillerm: das eeg-prinzip in der praxis: "ey chef! ich komme morgen eine stunde zur arbeit, will aber für 10 stunden bezahlt… ',
  'thu jul 20 12:25:02 +0000 2017',
  'michistelle'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 13:58:37 +0000 2017',
  'bernd471'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 14:47:09 +0000 2017',
  'plingl'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 14:46:01 +0000 2017',
  'mundaufmachen'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 16:11:17 +0000 2017',
  'uwebecher'),
 ('rt @espendillerm: das eeg-prinzip in der praxis: "ey chef! ich komme morgen eine stunde zur arbeit, will aber für 10 stunden bezahlt… ',
  'thu jul 20 11:52:01 +0000 2017',
  'regionalreport'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 13:31:49 +0000 2017',
  'afdduesseldorf'),
 ('rt @espendillerm: das eeg-prinzip in der praxis: "ey chef! ich komme morgen eine stunde zur arbeit, will aber für 10 stunden bezahlt… ',
  'thu jul 20 13:07:13 +0000 2017',
  'grandel1'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:31:03 +0000 2017',
  'paulplotzer'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 21:04:27 +0000 2017',
  'tartilleri'),
 ('rt @espendillerm: endlich! erst rettet die eu uns vor den staubsaugern, jetzt vor pommes. denkt an die millionen staubsaugeropfer!… ',
  'thu jul 20 21:05:28 +0000 2017',
  'tartilleri'),
 ('rt @espendillerm: das eeg-prinzip in der praxis: "ey chef! ich komme morgen eine stunde zur arbeit, will aber für 10 stunden bezahlt… ',
  'thu jul 20 21:06:35 +0000 2017',
  'tartilleri'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:17:15 +0000 2017',
  'darkynanmp'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 13:06:49 +0000 2017',
  'loose_afd'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:30:11 +0000 2017',
  'peterbeta69'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 11:54:33 +0000 2017',
  'erhardtresch'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:36:09 +0000 2017',
  'tonkhonkey'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 13:29:31 +0000 2017',
  'isidormeyer1'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:11:59 +0000 2017',
  'iamarealrealist'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 13:17:27 +0000 2017',
  'magna_est'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 13:37:56 +0000 2017',
  'chungun88'),
 ('rt @espendillerm: mist! die schweizer haben uns den ersten platz gestohlen. das ändern wir: #afd #btw17 #germanyfirst https://t.co/qtr4slmt…',
  'thu jul 20 12:59:25 +0000 2017',
  'ueberflug'),
 ('rt @politik_zz: #btw17: #merkel hat null ahnung v. thema #schule u. #migranten. als lehrer weiß ich, wovon ich rede und wähle  #afd! https:…',
  'thu jul 20 16:14:51 +0000 2017',
  'thomasboro'),
 ('rt @xnews24: rt "rt alice_weidel: #traudichdeutschland und zeige bei der #btw17 mit deiner stimme für die #afd, dass nichts in … https://t.…',
  'thu jul 20 17:34:45 +0000 2017',
  'traudichde'),
 ('rt @xnews24: rt marcuspretzell "#traudichdeutschland\n\n https://t.co/0zixew1r7o"',
  'thu jul 20 21:17:19 +0000 2017',
  'traudichde'),
 ('rt @btwahltrend: #wochentrend\n#spd, #cdu &amp; #grüne verlieren leicht, #linke legt zu, #fdp &amp; #afd  dicht beeinander… ',
  'thu jul 20 12:08:43 +0000 2017',
  'heischonin'),
 ('rt @v_palme: #merkel ist eine epochale fehlbesetzung u. sollte statt wiederwahl vor gericht stehen. #fedidwgugl #cdu #csu #btw17… ',
  'thu jul 20 11:39:21 +0000 2017',
  'zufallszahl'),
 ('rt @v_palme: #merkel ist eine epochale fehlbesetzung u. sollte statt wiederwahl vor gericht stehen. #fedidwgugl #cdu #csu #btw17… ',
  'thu jul 20 11:39:30 +0000 2017',
  'paulahasi13'),
 ('rt @v_palme: #gruene sind im kern eine faschistische partei u. #goeringeckardt ist die dümmste kandidatin aller zeiten!… ',
  'thu jul 20 17:34:41 +0000 2017',
  'paulahasi13'),
 ('rt @joeygerlach: wir erkennen unsere schweine am gang\n#afd #btw17 https://t.co/qa4qao3xcw',
  'thu jul 20 15:06:25 +0000 2017',
  'zufallszahl'),
 ('rt @joeygerlach: wir erkennen unsere schweine am gang\n#afd #btw17 https://t.co/qa4qao3xcw',
  'thu jul 20 13:50:23 +0000 2017',
  'peterpa34083139'),
 ('rt @joeygerlach: eine kleine entscheidungshilfe\n#afd #btw17 https://t.co/cse6amk5r1',
  'thu jul 20 12:44:43 +0000 2017',
  'ollimike'),
 ('rt @joeygerlach: wir erkennen unsere schweine am gang\n#afd #btw17 https://t.co/qa4qao3xcw',
  'thu jul 20 14:31:18 +0000 2017',
  'ollimike'),
 ('rt @joeygerlach: eine kleine entscheidungshilfe\n#afd #btw17 https://t.co/cse6amk5r1',
  'thu jul 20 13:26:41 +0000 2017',
  'bernd471'),
 ('rt @joeygerlach: das neue rot ist blau\n#afd #btw17 https://t.co/2qnx3ivr1l',
  'thu jul 20 13:30:10 +0000 2017',
  'bernd471'),
 ('rt @joeygerlach: damit können wir die welt retten\n#afd #btw17 https://t.co/qpgy6xauth',
  'thu jul 20 13:34:22 +0000 2017',
  'bernd471'),
 ('rt @joeygerlach: das neue rot ist blau\n#afd #btw17 https://t.co/2qnx3ivr1l',
  'thu jul 20 20:22:33 +0000 2017',
  'thomasboro'),
 ('rt @joeygerlach: eine kleine entscheidungshilfe\n#afd #btw17 https://t.co/cse6amk5r1',
  'thu jul 20 12:49:37 +0000 2017',
  '1netzreport'),
 ('rt @joeygerlach: damit können wir die welt retten\n#afd #btw17 https://t.co/qpgy6xauth',
  'thu jul 20 13:42:18 +0000 2017',
  'gerrywinkl'),
 ('rt @joeygerlach: wir erkennen unsere schweine am gang\n#afd #btw17 https://t.co/qa4qao3xcw',
  'thu jul 20 14:57:45 +0000 2017',
  'gerrywinkl'),
 ('rt @joeygerlach: wir erkennen unsere schweine am gang\n#afd #btw17 https://t.co/qa4qao3xcw',
  'thu jul 20 14:02:34 +0000 2017',
  'hevellia64'),
 ('rt @joeygerlach: das neue rot ist blau\n#afd #btw17 https://t.co/2qnx3ivr1l',
  'thu jul 20 12:41:04 +0000 2017',
  'derliuhvan'),
 ('rt @joeygerlach: damit können wir die welt retten\n#afd #btw17 https://t.co/qpgy6xauth',
  'thu jul 20 13:37:53 +0000 2017',
  'parteilos59'),
 ('rt @joeygerlach: das neue rot ist blau\n#afd #btw17 https://t.co/2qnx3ivr1l',
  'thu jul 20 12:41:10 +0000 2017',
  'kauflogos'),
 ("rt @afdduesseldorf: die studie bestätigt die kritik der #afd - an medien und flüchtlingspolitik. \n\nder kritische wähler wird's honorier… ",
  'thu jul 20 18:11:00 +0000 2017',
  'f_von_steiner'),
 ('rt @afdduesseldorf: osze schickt zur #btw17 wahlbeobachter nach 🇩🇪. \naber - 50 wahllokale beobachten reicht nicht. #afd \nhttps://t.co/gcdra…',
  'thu jul 20 18:37:25 +0000 2017',
  'paulplotzer'),
 ('rt @afdduesseldorf: osze schickt zur #btw17 wahlbeobachter nach 🇩🇪. \naber - 50 wahllokale beobachten reicht nicht. #afd \nhttps://t.co/gcdra…',
  'thu jul 20 18:54:55 +0000 2017',
  'leon_dnebach'),
 ('rt @afdduesseldorf: diw-studie zeigt: #afd ist die partei der arbeiter und selbständigen. #btw17  https://t.co/bipl3ydpi7',
  'thu jul 20 20:55:47 +0000 2017',
  'eusebius217'),
 ('rt @afd_hd: in #ladenburg stehen jetzt die plakatwände für die #btw17 – die #afd-plakate sind top-aktuell. #fdp will #vielfalt… ',
  'thu jul 20 19:29:10 +0000 2017',
  'peterpa34083139'),
 ('rt @afd_hd: in #ladenburg stehen jetzt die plakatwände für die #btw17 – die #afd-plakate sind top-aktuell. #fdp will #vielfalt… ',
  'thu jul 20 17:56:25 +0000 2017',
  'gomander2'),
 ('rt @andreasandy3131: ich nehme folgendes an: es ist nur #dielinke und deshalb wird die vorstellung nicht übertragen..\n@phoenix_de \n#btw17 h…',
  'thu jul 20 12:00:16 +0000 2017',
  'andreasandy3131'),
 ('rt @andreasandy3131: ich habe immer lust auf #dielinke! 🌹🌹 also kann man davon ausgehen, daß es einen livestream geben wird! 👍 #btw2017… ',
  'thu jul 20 13:47:45 +0000 2017',
  'andreasandy3131'),
 ('rt @andreasandy3131: deshalb wollen wir mit einer wahnsinnig starken #dielinke erwachen und neu aufblühen! 🌞 💥 ☄️ ✨\n#btw17\n#btw2017  https:…',
  'thu jul 20 14:08:49 +0000 2017',
  'andreasandy3131'),
 ('rt @andreasandy3131: damit alle informiert sind und danke für die antwort! 👍👍👍\n#dielinke \n#linksfraktion \n#btw17 \n#btw2017 https://t.co/msi…',
  'thu jul 20 15:42:39 +0000 2017',
  'andreasandy3131'),
 ('rt @andreasandy3131: ich nehme folgendes an: es ist nur #dielinke und deshalb wird die vorstellung nicht übertragen..\n@phoenix_de \n#btw17 h…',
  'thu jul 20 12:10:03 +0000 2017',
  'merteo1')]

for i in range(len(s["nodes"])):
    if s["nodes"][i]["label"] == 'megatwingo':
        print(s["nodes"][i])
RT_communities = []
for t in tweets:
    node_was_retweeted = t[0]
    node_was_retweeted = node_was_retweeted.split(":")
    node_was_retweeted = node_was_retweeted[0]
    node_was_retweeted = node_was_retweeted.lstrip("rt @")
    node_has_retweeted = t[2]
    for i in range(len(s["nodes"])):
        if s["nodes"][i]["label"] == node_was_retweeted:
            c = s["nodes"][i]["community"]
        if s["nodes"][i]["label"] == node_has_retweeted:
            cc = s["nodes"][i]["community"]
            RT_communities.append((node_was_retweeted, c, node_has_retweeted,cc))

RT_communities_V2 = [('espendillerm', 1, 'afd_support', 1),
 ('espendillerm', 1, 'megatwingo', 1),
 ('espendillerm', 1, 'derpatriot444', 2),
 ('espendillerm', 1, 'zufallszahl', 2),
 ('espendillerm', 1, 's_muenzenmaier', 1),
 ('espendillerm', 1, 'afd_hd', 1),
 ('espendillerm', 1, 'thomasraue', 2),
 ('espendillerm', 1, 'raluka19830803', 1),
 ('espendillerm', 1, 'traudichde', 1),
 ('espendillerm', 1, 'traudichde', 1),
 ('espendillerm', 1, 'traudichde', 1),
 ('espendillerm', 1, 'wicked777223', 1),
 ('espendillerm', 1, 'thomasgbauer', 3),
 ('espendillerm', 1, 'gomander2', 3),
 ('jochen_haug', 1, 'gomander2', 3),
 ('espendillerm', 1, 'michistelle', 2),
 ('espendillerm', 1, 'bernd471', 2),
 ('espendillerm', 1, 'plingl', 1),
 ('espendillerm', 1, 'mundaufmachen', 1),
 ('espendillerm', 1, 'uwebecher', 3),
 ('espendillerm', 1, 'regionalreport', 3),
 ('espendillerm', 1, 'afdduesseldorf', 1),
 ('espendillerm', 1, 'grandel1', 3),
 ('espendillerm', 1, 'paulplotzer', 2),
 ('espendillerm', 1, 'tartilleri', 1),
 ('espendillerm', 1, 'tartilleri', 1),
 ('espendillerm', 1, 'tartilleri', 1),
 ('espendillerm', 1, 'darkynanmp', 3),
 ('espendillerm', 1, 'loose_afd', 1),
 ('espendillerm', 1, 'peterbeta69', 1),
 ('espendillerm', 1, 'erhardtresch', 2),
 ('espendillerm', 1, 'tonkhonkey', 2),
 ('espendillerm', 1, 'isidormeyer1', 3),
 ('espendillerm', 1, 'iamarealrealist', 1),
 ('espendillerm', 1, 'magna_est', 1),
 ('espendillerm', 1, 'chungun88', 2),
 ('espendillerm', 1, 'ueberflug', 3),
 ('politik_zz', 2, 'thomasboro', 2),
 ('xnews24', 1, 'traudichde', 1),
 ('xnews24', 1, 'traudichde', 1),
 ('btwahltrend', 0, 'heischonin', 0),
 ('v_palme', 2, 'zufallszahl', 2),
 ('v_palme', 2, 'paulahasi13', 1),
 ('v_palme', 2, 'paulahasi13', 1),
 ('joeygerlach', 2, 'zufallszahl', 2),
 ('joeygerlach', 2, 'peterpa34083139', 3),
 ('joeygerlach', 2, 'ollimike', 2),
 ('joeygerlach', 2, 'ollimike', 2),
 ('joeygerlach', 2, 'bernd471', 2),
 ('joeygerlach', 2, 'bernd471', 2),
 ('joeygerlach', 2, 'bernd471', 2),
 ('joeygerlach', 2, 'thomasboro', 2),
 ('joeygerlach', 2, '1netzreport', 3),
 ('joeygerlach', 2, 'gerrywinkl', 2),
 ('joeygerlach', 2, 'gerrywinkl', 2),
 ('joeygerlach', 2, 'hevellia64', 2),
 ('joeygerlach', 2, 'derliuhvan', 3),
 ('joeygerlach', 2, 'parteilos59', 3),
 ('joeygerlach', 2, 'kauflogos', 2),
 ('afdduesseldorf', 1, 'paulplotzer', 2),
 ('afdduesseldorf', 1, 'leon_dnebach', 2),
 ('afdduesseldorf', 1, 'eusebius217', 1),
 ('afd_hd', 1, 'peterpa34083139', 3),
 ('afd_hd', 1, 'gomander2', 3),
 ('andreasandy3131', 0, 'andreasandy3131', 0),
 ('andreasandy3131', 0, 'andreasandy3131', 0),
 ('andreasandy3131', 0, 'andreasandy3131', 0),
 ('andreasandy3131', 0, 'andreasandy3131', 0),
 ('andreasandy3131', 0, 'merteo1', 0)]


RT_com_count = []
retweeted_user_com = []
retweeters_com = []
retweeters_tup = []
# e = 0
for i in RT_communities_V2:
    if i[1] == 0:
        # print(i[3])
        RT_com_count.append(i[3])
        # e = e + 1
        # print(e)
        # print(i[0], i[1], i[2], i[3])
        retweeted_user_com.append(i[0])
        retweeters_com.append(i[2])
        retweeters_tup.append((i[2], i[3]))

Counter(RT_com_count)
set(retweeted_user_com)
len(set(retweeters_com))


Counter(retweeters_tup)

set(retweeted_user_com)


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

b1_new = []
for b in b1:
    if b != -1:
        b1_new.append(b)
    else:
        b1_new.append(-0.1)

b2_new = []
for b in b2:
    if b != -1:
        b2_new.append(b)
    else:
        b2_new.append(-0.1)

bubbliness_new = []
for b in bubbliness:
    if b!= -1:
        bubbliness_new.append(b)
    else:
        bubbliness_new.append(-0.1)


Counter(times_retweeted)

times_retweeted_log = []
for i in times_retweeted:
    times_retweeted_log.append(math.log(1+i))

times_retweet_log = []
for i in times_retweet:
    times_retweet_log.append(math.log(1+i))

times_retweet_log

Counter(times_retweet_log)
times_retweeted_log

Counter(times_retweeted_2)


bubbliness_viz


def plot_scatter(col, title, t):
    x = xs
    y = ys
    s = 100
    my_dpi = 96
    plt.figure(figsize=(897/my_dpi, 721/my_dpi), dpi=my_dpi)
    plt.scatter(x, y, alpha=1, s=s, c=col, cmap="Greys", edgecolor='black', linewidth='1')
    plt.title('#BTW17 - ' + title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 897)
    plt.ylim(0, 721)
    plt.autoscale(False)
    plt.gca().invert_yaxis()
    plt.axis('off')
    if t != []:
        bar = plt.colorbar(ticks=t)
    # plt.savefig("BTW17_" + title + '_scatter.png', dpi=96, transparent=True)
    plt.show()
    # plt.draw()
    plt.close()

# plot_scatter(community, "Comm", [min(indegree), int(median(indegree)), max(indegree)])
# plot_scatter(indegree, "Nodes colored by indegree", [min(indegree), int(median(indegree)), max(indegree)])
# plot_scatter(outdegree, "Nodes colored by outdegree", [min(outdegree), int(median(outdegree)), max(outdegree)])
# plot_scatter(b1_new, "Nodes colored by containment at distance 1", [min(b1), int(median(b1)), max(b1)])
# plot_scatter(b2_new, "Nodes colored by containment at distance 2", [min(b2), int(median(b2)), max(b2)])
plot_scatter(bubbliness_viz, "Nodes colored by openness", [min(bubbliness), int(median(bubbliness)), max(bubbliness)])
# plot_scatter(times_retweeted_log, "Nodes colored by number of times they were retweeted", [min(times_retweeted_log), int(median(times_retweeted_log)), max(times_retweeted_log)])
# plot_scatter(times_retweet_log, "Nodes colored by number of times they retweeted", [min(times_retweet), int(median(times_retweet)), max(times_retweet)])

# communities scatters

def plot_com_scatter(title, xx, yy, c):
    x = xx
    y = yy
    s = 100
    my_dpi = 96
    plt.figure(figsize=(897/my_dpi, 721/my_dpi), dpi=my_dpi)
    plt.scatter(x, y, alpha=1, s=s, color=c, edgecolor='black', linewidth='1')
    plt.title('#BTW17 - ' + title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 897)
    plt.ylim(0, 721)
    plt.autoscale(False)
    plt.gca().invert_yaxis()
    plt.axis('off')
    plt.savefig("BTW17_" + title + '_scatter.png', dpi=96, transparent=True)
    plt.show()
    # plt.draw()
    plt.close()

# plot_com_scatter("Community 0", xs_0, ys_0, "#357AB1")
# plot_com_scatter("Community 1", xs_1, ys_1, "#B2C8E6")
# plot_com_scatter("Community 2", xs_2, ys_2, "#EF8637")
# plot_com_scatter("Community 3", xs_3, ys_3, "#F6BC80")
# plot_com_scatter("Community 4", xs_4, ys_4, "#57982C")

# histograms

def plot_hist(data, title, length, x, y):
    plt.figure(figsize=(200/96, 200/96), dpi=96)
    plt.hist(data, color="Grey", bins=length)
    # plt.title('#BTW17 - Statistics - ' + title + '\n  - Version du ' + str(time.asctime()))
    # plt.xlabel('Value of indegree')
    # plt.ylabel('Number of nodes')
    plt.xlim(-1, x)
    plt.ylim(0, y)
    plt.autoscale(False)
    plt.savefig("BTW17_" + title + '_histogram.png', dpi=96, transparent=True)
    plt.show()
    plt.close()

# plot_hist(indegree, "Indegree whole network", len(indegree), 55, 30)
# plot_hist(outdegree, "Outdegree whole network", len(outdegree),65,25)
# plot_hist(b1, "b1 whole network", len(b1), 1, 60)
# plot_hist(b2, "b2 whole network", len(b2), 1,30)
plot_hist(bubbliness, "openness ratio whole network", len(bubbliness), 1, 25)
# plot_hist(were_retweeted, "nodes were retweeted whole network", len(were_retweeted), 40, 2.1)
# plot_hist(have_retweeted, "nodes have retweeted whole network", len(have_retweeted), 5.1, 40)

# plot_hist(indegree_0, "Indegree community 0", len(indegree_0), 55, 15)
# plot_hist(outdegree_0, "Outdegree community 0", len(outdegree_0),65,25)
# plot_hist(b1_0, "b1 community 0", len(b1_0), 1, 40)
# plot_hist(b2_0, "b2 community 0", len(b2_0),1,30)
plot_hist(bubbliness_0, "openness ratio community 0", len(bubbliness_0), 1, 25)
# plot_hist(were_retweeted_0, "nodes were retweeted community 0", len(were_retweeted_0), 40, 40)
# plot_hist(have_retweeted_0, "nodes have retweeted community 0", len(have_retweeted_0), 5.1, 40)

# plot_hist(indegree_1, "Indegree community 1", len(indegree_1), 55, 15)
# plot_hist(outdegree_1, "Outdegree community 1", len(outdegree_1),65,25)
# plot_hist(b1_1, "b1 community 1", len(b1_1), 1, 40)
# plot_hist(b2_1, "b2 community 1", len(b2_1), 1,30)
plot_hist(bubbliness_1, "openness ratio community 1", len(bubbliness_1), 1, 25)
# plot_hist(were_retweeted_1, "nodes were retweeted community 1", len(were_retweeted_1), 40, 40)
# plot_hist(have_retweeted_1, "nodes have retweeted community 1", len(have_retweeted_1), 5.1, 40)

# plot_hist(indegree_2, "Indegree community 2", len(indegree_2), 55, 15)
# plot_hist(outdegree_2, "Outdegree community 2", len(outdegree_2),65,25)
# plot_hist(b1_2, "b1 community 2", len(b1_2), 1, 40)
# plot_hist(b2_2, "b2 community 2", len(b2_2), 1,30)
plot_hist(bubbliness_2, "openness ratio community 2", len(bubbliness_2), 1, 25)
# plot_hist(were_retweeted_2, "nodes were retweeted community 2", len(were_retweeted_2), 40, 40)
# plot_hist(have_retweeted_2, "nodes have retweeted community 2", len(have_retweeted_2), 5.1, 40)

# plot_hist(indegree_3, "Indegree community 3", len(indegree_3), 55, 15)
# plot_hist(outdegree_3, "Outdegree community 3", len(outdegree_3),65,25)
# plot_hist(b1_3, "b1 community 3", len(b1_3), 1, 40)
# plot_hist(b2_3, "b2 community 3", len(b2_3), 1,30)
plot_hist(bubbliness_3, "openness ratio community 3", len(bubbliness_3), 1, 25)
# plot_hist(were_retweeted_3, "nodes were retweeted community 3", len(were_retweeted_3), 40, 40)
# plot_hist(have_retweeted_3, "nodes have retweeted community 3", len(have_retweeted_3), 5.1, 40)

# plot_hist(indegree_4, "Indegree community 4", len(indegree_4), 55, 15)
# plot_hist(outdegree_4, "Outdegree community 4", len(outdegree_4),65,25)
# plot_hist(b1_4, "b1 community 4", len(b1_4), 1, 40)
# plot_hist(b2_4, "b2 community 4", len(b2_4), 1,30)
plot_hist(bubbliness_4, "openness ratio community 4", len(bubbliness_4), 1, 25)
# plot_hist(were_retweeted_4, "nodes were retweeted community 4", len(were_retweeted_4), 40, 40)
# plot_hist(have_retweeted_4, "nodes have retweeted community 4", len(have_retweeted_4), 5.1, 40)


#
bbb = []

for b in bubbliness:
    if b > 0:
        bbb.append(float(-b))
    if b == 0:
        bbb.append(1)

    if b < 0:
        bbb.append(1)

bbb
bubbliness

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
    plt.title('#BTW17 - ' + title)
    plt.axis('off')
    plt.autoscale(False)
    # plt.colorbar()
    plt.savefig("BTW17_" + title + '_heatmap.png', dpi=200, transparent=True)
    #
    plt.show()
    plt.close

heatmap(xs, ys, b1, "Containment at distance 1")
heatmap(xs_0, ys_0, b1_0, "b1 community0")
heatmap(xs_1, ys_1, b1_1, "b1 community1")
heatmap(xs_2, ys_2, b1_2, "b1 community2")
heatmap(xs_3, ys_3, b1_3, "b1 community3")
heatmap(xs_4, ys_4, b1_4, "b1 community4")

heatmap(xs, ys, b2, "Containment at distance 2")
heatmap(xs_0, ys_0, b2_0, "b2 community0")
heatmap(xs_1, ys_1, b2_1, "b2 community1")
heatmap(xs_2, ys_2, b2_2, "b2 community2")
heatmap(xs_3, ys_3, b2_3, "b2 community3")
heatmap(xs_4, ys_4, b2_4, "b2 community4")

# heatmap(xs, ys, bbb, "Openness ratio")
heatmap(xs, ys, bubbliness_viz, "Élargissement")
heatmap(xs_0, ys_0, bubbliness_0, "bubbliness community0")
heatmap(xs_1, ys_1, bubbliness_1, "bubbliness community1")
heatmap(xs_2, ys_2, bubbliness_2, "bubbliness community2")
heatmap(xs_3, ys_3, bubbliness_3, "bubbliness community3")
heatmap(xs_4, ys_4, bubbliness_4, "bubbliness community4")

heatmap(xs, ys, times_retweeted, "Number of times nodes were retweeted")
heatmap(xs, ys, times_retweet, "Number of times nodes have retweeted")

# Histograms per node

nodes_stats = []
for i in range(len(s["nodes"])):
    nodes_stats.append((s["nodes"][i]["id"],s["nodes"][i]["outdegree"],s["nodes"][i]["links_inside_community_at_distance_2"] + s["nodes"][i]["links_outside_community_at_distance_2"],s["nodes"][i]["b1"],s["nodes"][i]["b2"],s["nodes"][i]["bubbliness"],s["nodes"][i]["community"]))


nodes_stats
# list_1 = [1]

z = 0
for i in range(len(nodes_stats)):
    t = (nodes_stats[i][1], nodes_stats[i][2])
    u = (nodes_stats[i][3], nodes_stats[i][4], nodes_stats[i][5])
    c = (nodes_stats[i][6])

    # print(t)

    def plot_hist_node(t, u, colors, title, com):
        fig, (ax1, ax2) = plt.subplots(figsize=(7, 4), ncols=2)
        # plt.figure(figsize=(500/96, 500/96), dpi=96)
        x = np.arange(2)
        y = np.arange(3)
        ax1.bar(x, t)
        ax2.bar(y, u)
        # ax1.xaxis.set_ticks(x, ('at distance 1', 'at distance 2'))
        # ax1.xticks(x, ('at distance 1', 'at distance 2'))
        ax1.set_xticklabels(["","at d1", "", "at d2"])
        ax2.set_xticklabels(["","b1", "b2", "bb"])
        ax1.set_title('Outdegree')
        ax2.set_title('Bubbliness')

        fig.suptitle('#BTW17 - Statistics - ' + title + str(z) + ' - community ' + str(com))
        # plt.xlabel('Value of indegree')
        # plt.ylabel('Number of nodes')
        # plt.xlim(0, 897)
        # plt.ylim(0, 721)
        # plt.autoscale(False)
        plt.savefig("BTW17_Community_" + str(com) + "_" + title + str(z) + '_histogram.png', dpi=96, transparent=True)
        # plt.show()
        plt.close()

    plot_hist_node(t, u, "#3F007D", "Node", c)
    z = z + 1

# for each node, find community for all nodes at distance 1

list_friends_d1_new = []
list_friends_d2_new = []
for i in range(len(s["nodes"])):
    list_friends_d1_in = (s["nodes"][i]["id"], json.loads(s["nodes"][i]["list_of_friends_inside_community_at_distance_1"]))
    list_friends_d1_out = (s["nodes"][i]["id"], json.loads(s["nodes"][i]["list_of_friends_outside_community_at_distance_1"]))
    list_friends_d2_in = (s["nodes"][i]["id"], json.loads(s["nodes"][i]["list_of_friends_inside_community_at_distance_2"]))
    list_friends_d2_out = (s["nodes"][i]["id"], json.loads(s["nodes"][i]["list_of_friends_outside_community_at_distance_2"]))
    # print(list_friends_d1[1][0])
    # print(list_friends_d1_out)
    for j in list_friends_d1_in[1]:
        # print((i, j, s["nodes"][j]["community"]))
        list_friends_d1_new.append((i, j, s["nodes"][j]["community"]))

    for j in list_friends_d1_out[1]:
        # print((i, j, s["nodes"][j]["community"]))
        list_friends_d1_new.append((i, j, s["nodes"][j]["community"]))

    for j in list_friends_d2_in[1]:
        # print((i, j, s["nodes"][j]["community"]))
        list_friends_d2_new.append((i, j, s["nodes"][j]["community"]))

    for j in list_friends_d2_out[1]:
        # print((i, j, s["nodes"][j]["community"]))
        list_friends_d2_new.append((i, j, s["nodes"][j]["community"]))

list_friends_radar_d1 = []
list_friends_radar_d2 = []
list_friends_radar_d1_t = []
list_friends_radar_d2_t = []

for i in range(len(s["nodes"])):
    def radar_node(k):
        l = []
        m = []
        for n in list_friends_d1_new:
            if n[0] == k:
                # print(i)
                l.append(n[2])
                c = Counter(l)
                m = (k, s["nodes"][k]["community"], c)
        list_friends_radar_d1_t.append(m)
        if m != []:
            list_friends_radar_d1.append(m)

    radar_node(i)

for r in range(len(s["nodes"])):
    def radar_node(k):
        l = []
        m = []
        for n in list_friends_d2_new:
            if n[0] == k:
                # print(i)
                l.append(n[2])
                c = Counter(l)
                m = (k, s["nodes"][k]["community"], c)
        list_friends_radar_d2_t.append(m)
        if m != []:
            list_friends_radar_d2.append(m)

    radar_node(r)

list_friends_radar_d1d2 = []
for i in list_friends_radar_d1_t:
    try:
        j = i[0], i[1], i[2], list_friends_radar_d2_t[i[0]][2]
        list_friends_radar_d1d2.append(j)
    except:
        TypeError

len(list_friends_radar_d1)
len(list_friends_radar_d2)
len(list_friends_radar_d1d2)

len(list_friends_radar_d1_t)
len(list_friends_radar_d2_t)

# Donut distance 1

 for i in list_friends_radar_d1:
    try:
        c0_1 = (i[0], i[1], i[2][0])
        c1_1 = (i[0], i[1], i[2][1])
        c2_1 = (i[0], i[1], i[2][2])
        c3_1 = (i[0], i[1], i[2][3])
        c4_1 = (i[0], i[1], i[2][4])
        # print(c0)
    except:
        TypeError

    def plot_radar_node_d1(a,b,c,d,e,com,l):

        # The slices will be ordered and plotted counter-clockwise.
        labels = '0', '  1', '    2', '      3', '        4'
        sizes = [a,b,c,d,e]
        colors = ['#357AB1', '#B2C8E6', '#EF8637', '#F6BC80', '#57982C']
        explode = (0, 0, 0, 0, 0)  # explode a slice if required

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=False)

        #draw a circle at the center of pie to make it look like a donut
        centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=0.25)
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        plt.title('#BTW17 - Community Donut at d1 - Node ' + str(l) + ' - Community ' + str(com))
        # plt.savefig("BTW17_Community_" + str(com) + "_Node" + str(l) + '_donut_distance1.png', dpi=96, transparent=True)
        # Show polar plot
        plt.show()
        plt.close()

    plot_radar_node_d1(c0_1[2], c1_1[2], c2_1[2], c3_1[2], c4_1[2], c0_1[1], c0_1[0])

# Donut distance 2

for i in list_friends_radar_d2:
    try:
        c0_1 = (i[0], i[1], i[2][0])
        c1_1 = (i[0], i[1], i[2][1])
        c2_1 = (i[0], i[1], i[2][2])
        c3_1 = (i[0], i[1], i[2][3])
        c4_1 = (i[0], i[1], i[2][4])

        # print(c0)
    except:
        TypeError

    def plot_radar_node_d2(a,b,c,d,e,com,l):

        # The slices will be ordered and plotted counter-clockwise.
        labels = '0', '  1', '    2', '      3', '        4'
        sizes = [a,b,c,d,e]
        colors = ['#357AB1', '#B2C8E6', '#EF8637', '#F6BC80', '#57982C']
        explode = (0, 0, 0, 0, 0)  # explode a slice if required

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=False)

        #draw a circle at the center of pie to make it look like a donut
        centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=0.25)
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        plt.title('#BTW17 - Community Donut at d2 - Node ' + str(l) + ' - Community ' + str(com))
        # Show polar plot
        plt.savefig("BTW17_Community_" + str(com) + "_Node" + str(l) + '_donut_distance2.png', dpi=96, transparent=True)
        plt.show()
        plt.close()

    plot_radar_node_d2(c0_1[2], c1_1[2], c2_1[2], c3_1[2], c4_1[2], c0_1[1], c0_1[0])

# donuts d1 and d2
len(list_friends_radar_d1d2)
list_herfindhal = []

for i in list_friends_radar_d1d2:
    c = ((i[2][0])**2) + ((i[2][1])**2) + ((i[2][2])**2) + ((i[2][3])**2) + ((i[2][4])**2)
    d = ((i[3][0])**2) + ((i[3][1])**2) + ((i[3][2])**2) + ((i[3][3])**2) + ((i[3][4])**2)
    e = ((i[2][0]) + (i[2][1]) + (i[2][2]) + (i[2][3]) + (i[2][4]) + (i[3][0]) + (i[3][1]) + (i[3][2]) + (i[3][3]) + (i[3][4]))
    h = c
    list_herfindhal.append(h)

list_friends_radar_d1d2

list_friends_radar_d1d2.append(list_herfindhal)
# list_friends_radar_d1d2[117][0]

zzz = 0
for i in list_friends_radar_d1d2:
    try:
        c0_2 = (i[0], i[1], i[2][0], i[3][0])
        c1_2 = (i[0], i[1], i[2][1], i[3][1])
        c2_2 = (i[0], i[1], i[2][2], i[3][2])
        c3_2 = (i[0], i[1], i[2][3], i[3][3])
        c4_2 = (i[0], i[1], i[2][4], i[3][4])
        her = (list_friends_radar_d1d2[117][zzz])

    except:
        TypeError

    def pie(a,b,c,d,e,f,g,h,i,j,k,l,m):
            # Group colors
            com0 = '#357AB1'
            com1 = '#B2C8E6'
            com2 = '#EF8637'
            com3 = '#F6BC80'
            com4 = '#57982C'

            fig, ax = plt.subplots()
            ax.axis('equal')
            width = 0.3

            # cm = plt.get_cmap("tab20c")
            # cout = cm(np.arange(3)*4)
            pie, _ = ax.pie([a,b,c,d,e], radius=1, colors=[com0, com1, com2, com3, com4])
            plt.setp( pie, width=0.3, edgecolor='white')

            # cin = cm(np.array([1,2,5,6,9,10]))
            # labels = map("".join, zip(list("aabbcc"),map(str, [1,2]*3)))
            pie2, _ = ax.pie([f,g,h,i,j], radius=1-width/1.1, colors=[com0, com1, com2, com3, com4])
            plt.setp( pie2, width=0.7, edgecolor='white')
            # plt.title('#BTW17 - Horizon - Node ' + str(l) + ' - Community ' + str(k) + ' - Herfindhal ' + str(m))
            plt.savefig("BTW17_Community_" + str(k) + "_Herfindhal" + str(her) + "_Node" + str(l) + '_donut_distance_1and2.png', dpi=96, transparent=True)
            plt.show()
            plt.close()

    zzz = zzz + 1
    pie(c0_2[3],c1_2[3],c2_2[3],c3_2[3],c4_2[3], c0_2[2],c1_2[2],c2_2[2],c3_2[2],c4_2[2], c0_2[1], i[0], her)

# Communities heatmaps

def heatmap_xy(xx, yy, ww, title):
    x = xx
    y = yy
    my_dpi = 96
    # plt.subplot(5,1,2)
    plt.figure(figsize=(500/my_dpi, 500/my_dpi), dpi=my_dpi)
    # heatmap, xedges, yedges = np.histogram2d(x, y, bins=100, weights=ww)
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.gca().invert_yaxis()
    # fig, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.imshow(heatmap, interpolation='none')
    # ax2.imshow(convolve(heatmap, Gaussian2DKernel(stddev=10)), interpolation='none')
    # plt.title('#BTW17 - ' + title + '  - Version du ' + str(time.asctime()))
    # plt.axis('off')
    plt.autoscale(False)
    # plt.xticks(np.arange(0, max(x)*100+1, 10))
    # plt.yticks(np.arange(0, max(x)*100+1, 10))
    plt.scatter(x,y, )
    plt.xlabel('Containment at distance 1')
    plt.ylabel('Containment at distance 2')
    plt.plot((-1, 100, 100), (-1,100,100), "r--")
    # plt.colorbar()
    plt.savefig("BTW17_" + title + '_scatter.png', dpi=96, transparent=True)
    #
    plt.show()
    plt.close

heatmap_xy(0,0,0, "Community 0 - Containement differences")
heatmap_xy(b1_1, b2_1, bubbliness_1, "Community 1 - Containement differences")
heatmap_xy(b1_2, b2_2, bubbliness_2, "Community 2 - Containement differences")
heatmap_xy(b1_3, b2_3, bubbliness_3, "Community 3 - Containement differences")

heatmap_xy(b1_4, b2_4, bubbliness_4, "Community 4 - Containement differences")

# heatmap_xy(bubbliness_0, bubbliness_0, bubbliness_0, "bubbliness community 0")
# heatmap_xy(bubbliness_1, bubbliness_1, bubbliness_1, "bubbliness community 1")
# heatmap_xy(bubbliness_2, bubbliness_2, bubbliness_2, "bubbliness community 2")
# heatmap_xy(bubbliness_3, bubbliness_3, bubbliness_3, "bubbliness community 3")
# heatmap_xy(bubbliness_4, bubbliness_4, bubbliness_4, "bubbliness community 4")
