import json
import pandas

tweets_data = []
tweets_file = open('fetched_tweets_raw_2.json', 'r')

for line in tweets_file:
    try:
        if line.startswith('{"c'):
            tweet = json.loads(line)
            tweets_data.append(tweet)
    except:
        pass

# print(len(tweets_data))

# tweet = tweets_data[0]
# print(tweet)

# ids = [tweet['id_str'] for tweet in tweets_data]
# texts = [tweet['text'] for tweet in tweets_data]
# times = [tweet['created_at'] for tweet in tweets_data]
# screen_names = [tweet['user']['screen_name'] for tweet in tweets_data]
# names = [tweet['user']['name'] for tweet in tweets_data]
# hashtag1 = [(T['entities']['hashtags'][0]['text'] if len(T['entities']['hashtags']) >= 1 else None) for T in tweets_data]
# url1 = [(T['entities']['urls'][0]['expanded_url'] if len(T['entities']['urls']) >= 1 else None) for T in tweets_data]
# place_name = [(T['place']['full_name'] if T['place'] else None) for T in tweets_data]
# place_type = [(T['place']['place_type'] if T['place'] else None) for T in tweets_data]

# print(ids)
# print(texts)
# print(times)
# print(screen_names)
# print(names)
# print(hashtag1)
# print(urls)
# print(place_name)


tweets = pandas.DataFrame()
tweets['id'] = [tweet['id_str'] for tweet in tweets_data]
tweets['text'] = [tweet['text'] for tweet in tweets_data]
tweets['time'] = [tweet['created_at'] for tweet in tweets_data]
tweets['screen_name'] = [tweet['user']['screen_name'] for tweet in tweets_data]
tweets['name'] = [tweet['user']['name'] for tweet in tweets_data]
tweets['user id'] = [tweet['user']['id'] for tweet in tweets_data]
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
tweets['retweet'] = [tweet['current_user_retweet']['id_str'] for tweet in tweets_data]

tweets.to_csv('prova_3.csv')