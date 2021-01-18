import tweepy
import tokens
import time

auth = tweepy.OAuthHandler(tokens.consumer_key, tokens.consumer_secret)
auth.set_access_token(tokens.access_token, tokens.access_token_secret)

api = tweepy.API(auth)
modi = 'narendramodi'

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
    #friend_ids = []
    i=0
    for friend in limit_handled(tweepy.Cursor(api.friends, screen_name=user).items()):
        print(friend.screen_name)
        # i+=1
        # if i > 4:
        #     break

def main():
    user = modi
    get_friends(modi)

if __name__ == '__main__':
    main()
