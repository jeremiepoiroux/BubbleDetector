import time
import tweepy
from credentials_bubblebot import *
import os

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Filters
keywords = ['twitter']

# Stream Listener


class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        print(data)
        with open('fetched_tweets_raw.txt', 'a') as tf:
            tf.write(data)
            tf.write('\n')
        with open('fetched_tweets_raw.json', 'a') as tf:
            tf.write(data)
            tf.write('\n')
        return True

    def on_error(self, status):
        print(status)


# This handles Twitter authentication and the connection to Twitter Streaming API
if __name__ == '__main__':
    SOL = StdOutListener()
    stream = tweepy.Stream(auth, SOL)
    stream.filter(track=keywords, languages=['fr'])
