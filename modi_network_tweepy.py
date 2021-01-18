import tweepy
import tokens

auth = tweepy.OAuthHandler(tokens.consumer_key, tokens.consumer_secret)
auth.set_access_token(tokens.access_token, tokens.access_token_secret)

api = tweepy.API(auth)

# link on handling rate limits with cursors:
# https://github.com/tweepy/tweepy/blob/master/docs/code_snippet.rst#pagination

#tweepy docs:
# https://docs.tweepy.org/en/latest/index.html

def limit_handled(cursor):
    while True:
        try:
            yield next(cursor)
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

def get_friends(user):
    friend_ids = []
    i = 0

    cursor = limit_handled(tweepy.Cursor(api.friends(user)).items())
    for friend in cursor:
        if i < 10:
            print(friend.screen_name)
        else:
            break
        i = i + 1

user = 'narendramodi'
get_friends(user)
