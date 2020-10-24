import tweepy
import time

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'

key = 'your_key'
secret = 'your_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = '@python' #change it, if you want
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print('Retweet done!')
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

if __name__ == '__main__':
    searchBot()
