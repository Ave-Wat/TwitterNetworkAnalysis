#https://realpython.com/twitter-bot-python-tweepy/

import tweepy
import tokens

auth = tweepy.OAuthHandler(tokens.consumer_key, tokens.consumer_secret)
auth.set_access_token(tokens.access_token, tokens.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

i = 0
for tweet in public_tweets:
    if i > 2:
        break
    else:
        i = i + 1
        print(tweet.text)
        print()
