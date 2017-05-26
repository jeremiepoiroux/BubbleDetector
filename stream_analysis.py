import json
import pandas
import matplotlib.pyplot as plt
import re

# Use data from file
tweets_data_path = 'twitter_data.txt'

# Read file
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)

    except:
        continue

# Print number of tweets
print(len(tweets_data))

# Create DataFrame
tweets = pandas.DataFrame()

# Create data columns



def word_in_text(word, text):
    word = str.lower(word)
    text = str.lower(text)
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))

print(tweets['python'].value_counts()[True])
print(tweets['javascript'].value_counts()[True])
print(tweets['ruby'].value_counts()[True])
