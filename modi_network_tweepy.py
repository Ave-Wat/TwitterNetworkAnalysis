import tweepy
import tokens

auth = tweepy.OAuthHandler(tokens.consumer_key, tokens.consumer_secret)
auth.set_access_token(tokens.access_token, tokens.access_token_secret)

api = tweepy.API(auth)

# link on handling rate limits with cursors:
# https://github.com/tweepy/tweepy/blob/master/docs/code_snippet.rst#pagination

cursor = tweepy.Cursor(api.followers_ids, id = 'narendramodi')

i = 0
modi_following = []
for page in cursor.pages():
     ids.append(page)

for tweet in public_tweets:
    if i > 2:
        break
    else:
        i = i + 1
        print(tweet.text)
        print()
