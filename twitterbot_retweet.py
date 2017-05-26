# Import our Twitter credentials from credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search,
                           q='#ocean',
                           since='2016-11-25',
                           until='2016-11-75',
                           geocode='1.3552217,103.8231561,100km',
                           lang='fr').items():
    try:
        # Print out usernames of the last 10 people to use #ocean
        print('\nTweet by: @' + tweet.user.screen_name)
        tweet.retweet()
        print('Retweeted the tweet')
        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
