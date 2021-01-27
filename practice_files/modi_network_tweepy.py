import tweepy
import tokens
import time

auth = tweepy.OAuthHandler(tokens.consumer_key, tokens.consumer_secret)
auth.set_access_token(tokens.access_token, tokens.access_token_secret)

api = tweepy.API(auth)
modi = 'narendramodi'

def limit_handled(cursor):
    while True:
        try:
            yield next(cursor)
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

def get_friends(user):
    #friend_ids = []
    i=0
    #limits us at 300; have to wait 15 mins; to avoid for practice, uncomment if/break with int i
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
