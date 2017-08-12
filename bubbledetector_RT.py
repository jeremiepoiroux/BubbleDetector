import igraph as ig
import codecs
import csv
import pandas as pd

# take files
csv_file = input ("Which CSV file (with _tweets.csv)?: ")
gml_file = input ("Which GML file (with _def.gml)?: ")

df = pd.read_csv(csv_file, error_bad_lines=False)  # read file from stream

g = ig.Graph.Read_GML(gml_file)

# Who retweeted
csv_screen_names = []
for i in df["screen_names"]:
    csv_screen_names.append(i)

csv_screen_names_set = set(csv_screen_names)
len(csv_screen_names)
len(csv_screen_names_set)

# Who was retweeted

tweets = []
for i in df.text:
    if i.startswith( "RT" ):
        tweets.append(i)

len(tweets)

tweets_RT = []
for t in tweets:
    t = t.split(":")
    t = t[0]
    t = t.lstrip("RT @")
    tweets_RT.append(t)

len(tweets_RT)
tweets_RT_set = set(tweets_RT)
len(tweets_RT_set)

users_RT = []
for i in csv_screen_names_set:
    if i in tweets_RT_set:
        users_RT.append(i)

len(users_RT)

gml_screen_names = []
for i in g.vs["label"]:
    gml_screen_names.append(i)

gml_screen_names_set = set(gml_screen_names)
len(gml_screen_names)
len(gml_screen_names_set)

retweeted = []
for i in users_RT:
    if i in gml_screen_names:
        retweeted.append(i)

print("retweeted: " + str(len(retweeted)))

retweeters = []
for i in csv_screen_names_set:
    if i in gml_screen_names:
        retweeters.append(i)

print("retweeters: " + str(len(retweeters)))

# for i in df.text:
    # for r in retweeted:
        # if r in i and "RT" in i:
            # print(i)

# for i in df.text:
    # for r in retweeters:
        # if r in i and "RT" in i:
            # print(i)
