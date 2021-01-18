#https://realpython.com/twitter-bot-python-tweepy/
#https://docs.tweepy.org/en/v3.4.0/install.html
# link on handling rate limits with cursors:
# https://github.com/tweepy/tweepy/blob/master/docs/code_snippet.rst#pagination
#tweepy docs: https://docs.tweepy.org/en/latest/index.html

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
