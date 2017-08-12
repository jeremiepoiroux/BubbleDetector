# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from time import gmtime, strftime
import codecs
import sys


# Access and authorize our Twitter credentials from credentials.py
access_token = "XXX"
access_token_secret = "XXX"
consumer_key = "XXX"
consumer_secret = "XXX"


# Filters
keywords = input ("Which keyword?: ")
keywords = [keywords]

# Name of files
day = strftime("%Y-%m-%d", gmtime())
file_name = str(keywords[0]) + '_' + day

# This is a basic listener that just prints received tweets to stdout.
n = 1


class StdOutListener(StreamListener):

    def on_connect(self):
        pass

    def on_data(self, data):
        global n
        print(n)
        n = n + 1
        with codecs.open("/home/data/poiroux/" + file_name + '.json', 'a', 'utf-8') as tf:
            tf.write(data)
            tf.write('\n')  # Add one line per tweet to the .json file
        pass

        # Tweepy variables to deal with errors
    def keep_alive(self):
        return True

    def on_exception(self, exception):
        print(exception)
        pass

    def on_limit(self, track):
        print(track)
        pass

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', status_code)
        pass # Don't kill the stream

    def on_AttributeError(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', status_code)
        pass # Don't kill the stream

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        pass # Don't kill the stream

    def on_disconnect(self, notice):
        print(notice)
        pass

    def on_warning(self, notice):
        print(notice)
        pass

if __name__ == '__main__':

    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=keywords, languages=["de"], async=True, stall_warnings=True)
