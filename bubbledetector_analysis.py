import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv('lyon_3.csv')
number_tweets = len(df.index)
number_tweets
columns = ['screen_names']
df1 = list(df.screen_names)
df1 = Counter(df1)
df1 = pd.DataFrame.from_dict(df1, orient='index').reset_index()
df1 = df1.rename(columns={'index':'screen names', 0:'number of tweets'})
df1['names'] = (df['names'])
df1['user id'] = (df['user id'])
df1['statuses count'] = (df['statuses count'])
df1['friends count'] = (df['friends count'])
df1['followers count'] = (df['followers count'])
df1 = df1.sort_values(by='number of tweets', ascending=False)
df1 = df1[['screen names', 'names', 'user id', 'statuses count', 'friends count', 'followers count', 'number of tweets']]
df1.to_csv('lyon_3_users.csv')
number_users = len(df1.index)
df1_mean = df1.mean(axis=0)
df1_min = df1.min(axis=0)
df1_max = df1.max(axis=0)
df1_var = df1.var(axis=0)
df1_std = df1.std(axis=0)
df1_median = df1.median(axis=0)
pc_number_users = int(number_users / 10)
pc_number_users
df2 = df1.iloc[0:pc_number_users]
df2.to_csv('lyon_3_users_10pc.csv')

print(str(number_tweets) + ' tweets from ' + str(number_users) + ' users')
print(df1_mean)
print(df1_median)
print(df1_var)
print(df1_std)
print(pc_number_users)

df1
df2
