# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from time import gmtime, strftime
import codecs


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


class StdOutListener(StreamListener):

    def on_connect(self):
        pass

    def on_data(self, data):
        with codecs.open(file_name + '.json', 'a', 'utf-8') as tf:
            tf.write(data)
            tf.write('\n')  # Add one line per tweet to the .json file


        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=keywords, async=True, stall_warnings=True)
