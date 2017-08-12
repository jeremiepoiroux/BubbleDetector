import igraph as ig
import codecs
import csv
import pandas as pd

# take files
csv_file = input ("Which CSV file (with .csv)?: ")
gml_file = input ("Which GML file (with .gml)?: ")

# read gml
g = ig.Graph.Read_GML(gml_file)

# read csv
df = pd.read_csv(csv_file, error_bad_lines=False)
len(df)
# grab the 125th line and the number of tweets of this user
df_loc = df.loc[300]
nb_tweets = df_loc["number_of_tweets"]
print(nb_tweets)

# create list of users with less than x tweets
df_new_inf = df[df.number_of_tweets <= nb_tweets]
df_new_inf = pd.Series(df_new_inf["user_id"])
df_new_inf = df_new_inf.tolist()

len(df_new_inf)

# create list of users with more than x tweets
df_new_sup = df[df.number_of_tweets > nb_tweets]
df_new_sup = pd.Series(df_new_sup["user_id"])
df_new_sup = df_new_sup.tolist()

len(df_new_sup)

# delete users in inf list if they are in sup list
# for u in df_new_inf:
    # if u in df_new_sup:
        # df_new_inf.remove(u)

len(df_new_inf)

# change integers into strings
list_of_users = []
for i in df_new_sup:
    j = str(i)
    list_of_users.append(j)

len(list_of_users)
# list_of_users_t = []

# create a list of users to delete
to_delete = []
list_of_users_set = set(list_of_users)
print(len(list_of_users_set))

for i in range(len(g.vs)):
    if g.vs[i]["user_id"] not in list_of_users:
        to_delete.append(i)

len(to_delete)
g.delete_vertices(to_delete)

# export new gml
g.save(gml_file + "_limited.gml", format="gml")
