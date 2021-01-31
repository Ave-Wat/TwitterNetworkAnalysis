import tweepy
import tokens
import time
import csv

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
        with open('usernames.csv', 'a+', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['narendramodi', friend.screen_name])
        file.close()

def main():
    user = modi
    get_friends(modi)

if __name__ == '__main__':
    main()
