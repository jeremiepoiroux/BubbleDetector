import pandas as pd
from collections import Counter
import numpy as np

# Define news files names
csv_file = input ("Which CSV file (without .csv)?: ")
file_name_users = csv_file + '_users'
# file_name_users_100 = file_name_users + '_100'

df = pd.read_csv(csv_file + '.csv', error_bad_lines=False)  # read file from stream

number_total_tweets = len(df.index)  # total number of tweets

columns = ['screen_names']  # transform the screen_names column to a list
df1 = list(df.screen_names)  # df1 is the new list
df1 = Counter(df1)  # count the number of tweets for each user
df1 = pd.DataFrame.from_dict(df1, orient='index').reset_index()  # transform the list to an array with one column for the names and one for the number of tweets
df1 = df1.rename(columns={'index': 'screen_names', 0: 'number_of_tweets'})  # rename the columns
number_users = len(df1)

# statistics about the number of tweets
df1_mean = df1.mean(axis=0)
df1_min = df1.min(axis=0)
df1_max = df1.max(axis=0)
df1_var = df1.var(axis=0)
df1_std = df1.std(axis=0)
df1_median = df1.median(axis=0)

# add columns to the new array
df1['names'] = (df['names'])
df1['user_id'] = (df['user id'])
# df1['statuses_count'] = (df['statuses count'])
# df1['friends_count'] = (df['friends count'])
df1['followers_count'] = (df['followers count'])
df1 = df1[['screen_names', 'names', 'user_id', 'followers_count', 'number_of_tweets']]
# df1 = df1[['screen_names', 'names', 'user_id', 'statuses_count', 'friends_count', 'followers_count', 'number_of_tweets']]

df1 = df1.sort_values(by='number_of_tweets', ascending=False)  # ascending sort of the users with users followers

df1.to_csv(file_name_users + '.csv')  # create csv file with all users

# Create a csv file with only the users with more than 100 followers
# df2 = df1[df1.followers_count > 100]
# df2.to_csv(file_name_users_100 + '.csv')
# number_of_users_100 = len(df2.index)

# Create a list with the screen names
screen_names = df1['screen_names']
users = list(screen_names)

# Export the screen names to a .twt file
users = ['@' + user for user in users]
with open(file_name_users + '.twt', 'a') as tf:
    for user in users:
        tf.write(str(user))
        tf.write('\n')

# Print statistics
print(str(number_total_tweets) + ' tweets from ' + str(number_users) + ' users')
print('ratio: ' + str((number_total_tweets/number_users)/100))
print('mean: ' + str(df1_mean))
print('median: ' + str(df1_median))
print('var: ' + str(df1_var))
print('std: ' + str(df1_std))
# print('number of users > 100 followers: ' + str(number_of_users_100))
# print('10%: ' + str(pc_number_users))
