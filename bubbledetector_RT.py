import igraph as ig
import codecs
import csv
import pandas as pd
import json

# take files
csv_file = input ("Which CSV file (with _tweets.csv)?: ")
gml_file = input ("Which GML file (with _def.gml)?: ")

df = pd.read_csv(csv_file, error_bad_lines=False)  # read file from stream
g = ig.Graph.Read_GML(gml_file)

# Who retweeted

gml_screen_names = []
for i in g.vs["label"]:
    gml_screen_names.append(i)

gml_screen_names_set = set(gml_screen_names)
len(gml_screen_names)
len(gml_screen_names_set)

####
df_list = df.values.tolist()

list_of_retweeters = []
list_of_tweets_retweeted = []

# test if no nan
# for d in df_list:
    # print(d[4].lower())

# delete nan
# del df_list[6779]
# df_list[6778]

for r in gml_screen_names:
    for d in df_list:
        if r in d[4].lower() and "rt @" in d[2].lower():
            list_of_tweets_retweeted.append((d[2].lower(),d[3].lower(),d[4].lower()))
        if r in d[4].lower():
            list_of_retweeters.append(r)

len(list_of_retweeters)
len(list_of_tweets_retweeted)

len(set(list_of_retweeters))
len(set(list_of_tweets_retweeted))

# set(list_of_retweeters)

###

list_of_people_retweeted = []
for t in list_of_tweets_retweeted:
    t = t[0]
    t = t.split(":")
    t = t[0]
    t = t.lstrip("rt @")
    # print(t)
    list_of_people_retweeted.append(t)

len(list_of_people_retweeted)
len(set(list_of_people_retweeted))
list_of_people_retweeted_set = set(list_of_people_retweeted)

# gml_screen_names_set
# list_of_people_retweeted_set

# Final list

list_of_people_retweeted_inside = []
for f in list_of_people_retweeted:
    if f in gml_screen_names:
            list_of_people_retweeted_inside.append(f)

len(set(list_of_people_retweeted_inside))
len(list_of_people_retweeted_inside)

list_of_people_retweeted_inside_set = set(list_of_people_retweeted_inside)

final_list = []
for i in list_of_people_retweeted_inside_set:
    for t in list_of_tweets_retweeted:
        if i in t[0]:
            final_list.append((t[0], t[1], t[2]))

len(final_list)
len(set(final_list))
final_list

final_list_retweeters = []
for f in final_list:
    final_list_retweeters.append(f[2])

len(set(final_list_retweeters))

print('stats \n' + str(len(set(final_list_retweeters))) + ' retweeters \n' + str(len(set(final_list))) + ' retweets \n' + str(len(set(list_of_people_retweeted_inside))) + ' retweeted people')


Counter(list_of_people_retweeted_inside)
Counter(final_list_retweeters)
