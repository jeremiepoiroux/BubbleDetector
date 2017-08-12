import json
import pandas

tweets_data = []
json_file = input ("Which JSON file (without .json)?: ")
tweets_file = open(json_file + ".json", 'r')  # open the .json file and take only the tweets from it
for line in tweets_file:
    try:
        if line.startswith('{"c'):
            tweet = json.loads(line)
            tweets_data.append(tweet)
    except:
        continue

tweets = pandas.DataFrame()  # create a dataframe with the following columns

tweets['ids'] = [tweet['id_str'] for tweet in tweets_data]
tweets['text'] = [tweet['text'] for tweet in tweets_data]
tweets['times'] = [tweet['created_at'] for tweet in tweets_data]
tweets['screen_names'] = [tweet['user']['screen_name'] for tweet in tweets_data]
tweets['user id'] = [tweet['user']['id'] for tweet in tweets_data]  # added
tweets['names'] = [tweet['user']['name'] for tweet in tweets_data]
# tweets['hashtag1'] = [(T['entities']['hashtags'][0]['text'] if len(T['entities']['hashtags']) >= 1 else None) for T in tweets_data]
# tweets['hashtag2'] = [(T['entities']['hashtags'][1]['text'] if len(T['entities']['hashtags']) >= 2 else None) for T in tweets_data]
# tweets['hashtag3'] = [(T['entities']['hashtags'][2]['text'] if len(T['entities']['hashtags']) >= 3 else None) for T in tweets_data]
# tweets['url1'] = [(T['entities']['urls'][0]['expanded_url'] if len(T['entities']['urls']) >= 1 else None) for T in tweets_data]
# tweets['url2'] = [(T['entities']['urls'][1]['expanded_url'] if len(T['entities']['urls']) >= 2 else None) for T in tweets_data]
# tweets['url3'] = [(T['entities']['urls'][2]['expanded_url'] if len(T['entities']['urls']) >= 3 else None) for T in tweets_data]
# tweets['in reply to screen name'] = [tweet['in_reply_to_screen_name'] for tweet in tweets_data]
# tweets['in reply to user id'] = [tweet['in_reply_to_user_id_str'] for tweet in tweets_data]
# tweets['in reply to status id'] = [tweet['in_reply_to_status_id_str'] for tweet in tweets_data]
# tweets['statuses count'] = [tweet['user']['statuses_count'] for tweet in tweets_data]
# tweets['friends count'] = [tweet['user']['friends_count'] for tweet in tweets_data]
tweets['followers count'] = [tweet['user']['followers_count'] for tweet in tweets_data]
# tweets['lang of the account'] = [tweet['user']['lang'] for tweet in tweets_data]
# tweets['location of the account'] = [tweet['user']['location'] for tweet in tweets_data]

tweets.to_csv(json_file + '.csv')  # export this dataframe to a csv file
