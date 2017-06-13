import tweepy
from time import sleep
from credentials_bubblebot import *
import sys
import json

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Query
query_string = 'han @karlpineau'
query_lang = ''
query_rpp = '100'
query_start = '2017-05-25'
query_stop = '2017-05-26'
query_geocode = ''

# Info
# tweet = '[Test] ' + 'Now I follow people who tweeted in *' + query_lang + '* about ' + query_string + ' 1/2 '
# api.update_status(status=tweet)

# last_tweet = api.user_timeline(screen_name='BubbleBot_', count='1')
# status = last_tweet[0]
# json_str = json.dumps(status._json)
# parsed_json = json.loads(json_str)
# last_tweet_id = parsed_json['id']

# tweet = '[Test] ' + 'From *' + query_start + '* to *' + query_stop + '* around this location: *' + query_geocode + '* 2/2 '
# api.update_status(status=tweet, in_reply_to_status_id=last_tweet_id)

# Search


for tweet in tweepy.Cursor(api.search, q=query_string, lang=query_lang, rpp=query_rpp, since=query_start, until=query_stop, geocode=query_geocode).items():
    try:
        print(tweet.user.screen_name)
        print(tweet.user.id)
        # Follow the user who tweeted
        # tweet.user.follow()
        # print('Followed the user')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
