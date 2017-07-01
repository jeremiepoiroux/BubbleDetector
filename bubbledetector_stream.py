# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from time import gmtime, strftime
import codecs
import sys


# Access and authorize our Twitter credentials from credentials.py
access_token = "868895998407573504-eVAVmibVVqmcPAoQSG9odzsQZpTTa3N"
access_token_secret = "uSTu7VM37mqlBzi6aM8kr0OcQFbIfDnwstvjkLGvaFHbL"
consumer_key = "bJ3rmlTYgZdLdu99zyW5zEcdu"
consumer_secret = "1lXmZP4gsnBri0IIWE0RM3PH9tmKofb4Un9VYIDAw2lNK10Inn"


# Filters
keywords = ['HarryPotter20']

# Name of files
day = strftime("%Y-%m-%d", gmtime())
file_name = day + '_' + str(keywords[0])

# This is a basic listener that just prints received tweets to stdout.
n = 0


class StdOutListener(StreamListener):

    def on_connect(self):
        pass

    def on_data(self, data):
        print(n + 1)
        with codecs.open(file_name + '.json', 'a', 'utf-8') as tf:
            tf.write(data)
            tf.write('\n')  # Add one line per tweet to the .json file
        return True

        # Tweepy variables to deal with errors
    def keep_alive(self):
        return True

    def on_exception(self, exception):
        print(exception)
        return True

    def on_limit(self, track):
        print(track)
        return True

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', status_code)
        return True  # Don't kill the stream

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True  # Don't kill the stream

    def on_disconnect(self, notice):
        print(notice)
        return True

    def on_warning(self, notice):
        print(notice)
        return True

if __name__ == '__main__':

    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=keywords, async=True, stall_warnings=True)
