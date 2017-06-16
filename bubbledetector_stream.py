import time
import tweepy
from credentials_bubblebot import *
import codecs
import json
import pandas
# import os

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Filters
keywords = ['lyon']

# Stream Listener


class StdOutListener(tweepy.StreamListener):

    def __init__(self, time_limit=600):
        self.start_time = time.time()
        self.limit = time_limit
        super(StdOutListener, self).__init__()

    def on_connect(self):
        pass

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            with codecs.open('fetched_tweets_raw_3.json', 'a', 'utf-8') as tf:
                tf.write(data)
                tf.write('\n')
            time_lapse = str((time.time() - self.start_time))
            time_lapse = time_lapse.split('.')
            time_lapse = int(time_lapse[0])

            tweets_data = []
            tweets_file = open('fetched_tweets_raw_3.json', 'r')
            for line in tweets_file:
                try:
                    if line.startswith('{"c'):
                        tweet = json.loads(line)
                        tweets_data.append(tweet)
                except:
                    pass
            print(str(len(tweets_data)) + " tweets for " + str(time_lapse) + " secs out of " + str(self.limit) + " - " + str((time_lapse/self.limit)*100) + ' %')

            tweets = pandas.DataFrame()

            tweets['ids'] = [tweet['id_str'] for tweet in tweets_data]
            tweets['text'] = [tweet['text'] for tweet in tweets_data]
            tweets['times'] = [tweet['created_at'] for tweet in tweets_data]
            tweets['screen_names'] = [tweet['user']['screen_name'] for tweet in tweets_data]
            tweets['user id'] = [tweet['user']['id'] for tweet in tweets_data]  # added
            tweets['names'] = [tweet['user']['name'] for tweet in tweets_data]
            tweets['hashtag1'] = [(T['entities']['hashtags'][0]['text'] if len(T['entities']['hashtags']) >= 1 else None) for T in tweets_data]
            tweets['hashtag2'] = [(T['entities']['hashtags'][1]['text'] if len(T['entities']['hashtags']) >= 2 else None) for T in tweets_data]
            tweets['hashtag3'] = [(T['entities']['hashtags'][2]['text'] if len(T['entities']['hashtags']) >= 3 else None) for T in tweets_data]
            tweets['url1'] = [(T['entities']['urls'][0]['expanded_url'] if len(T['entities']['urls']) >= 1 else None) for T in tweets_data]
            tweets['url2'] = [(T['entities']['urls'][1]['expanded_url'] if len(T['entities']['urls']) >= 2 else None) for T in tweets_data]
            tweets['url3'] = [(T['entities']['urls'][2]['expanded_url'] if len(T['entities']['urls']) >= 3 else None) for T in tweets_data]
            tweets['in reply to screen name'] = [tweet['in_reply_to_screen_name'] for tweet in tweets_data]
            tweets['in reply to user id'] = [tweet['in_reply_to_user_id_str'] for tweet in tweets_data]
            tweets['in reply to status id'] = [tweet['in_reply_to_status_id_str'] for tweet in tweets_data]
            tweets['statuses count'] = [tweet['user']['statuses_count'] for tweet in tweets_data]
            tweets['friends count'] = [tweet['user']['friends_count'] for tweet in tweets_data]
            tweets['followers count'] = [tweet['user']['followers_count'] for tweet in tweets_data]
            tweets['lang of the account'] = [tweet['user']['lang'] for tweet in tweets_data]
            tweets['location of the account'] = [tweet['user']['location'] for tweet in tweets_data]

            tweets.to_csv('lyon_3.csv')

            return True
        else:
            return False  # changed

    def keep_alive(self):
        return True

    def on_exception(self, exception):
        print(exception)
        return True

    def on_limit(self, track):
        print(track)
        return True

    def on_error(self, status):
        print(status)
        return True

    def on_timeout(self):
        return

    def on_disconnect(self, notice):
        print(notice)
        return

    def on_warning(self, notice):
        print(notice)
        return


# This handles Twitter authentication and the connection to Twitter Streaming API
if __name__ == '__main__':
    SOL = StdOutListener()
    stream = tweepy.Stream(auth, SOL)
    stream.filter(track=keywords, languages=['fr'], async=True)

