# !/usr/bin/python3.6
import tweepy
from tweepy.streaming import StreamListener
from credentials import*

# Authentication
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.secure = True
# authUrl = auth.get_authorization_url()

# Visit URL
# print('Please Visit This link and authorize the app ==> ' + authUrl)
# pin = input('Enter The Authorization PIN: ')

# Writing access tokes to credentials file
# token = auth.get_access_token(verifier=pin)
# credentials = open('credentials.py', 'a')
# credentials.write('\n' + 'access_token = \'' + token[0] + '\' \n')
# credentials.write('access_token_secret = \'' + token[1] + '\' \n')
# credentials.close()

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth)

# Tests


class TweetListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


class StdOutListener(StreamListener):

    def on_data(self, data):
        with open('fetched_tweets.txt', 'a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)

mystream = tweepy.Stream(auth, TweetListener())
mystream.filter(track=['python'])

