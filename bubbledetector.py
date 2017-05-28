import tweepy
from time import sleep
from credentials_bubblebot import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Tweet
# tweet = 'XXX'
# api.update_status(status=tweet)

