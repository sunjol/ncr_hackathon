from config import *
import tweepy
import datetime
import pandas as pd
auth=tweepy.OAuthHandler(TWITTER_CONSUMER_KEY,TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_TOKEN_SECRET)
api=tweepy.API(auth,wait_on_rate_limit=True)
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
tweets_list = tweepy.Cursor(api.search, q="#Covid-19 AND #India since:" + str(yesterday)+ " until:" + str(today),tweet_mode='extended',lang="en").items()
output=[]
x=0
for tweet in tweets_list :
    if(not tweet.retweeted) and ('RT @' not in tweet.full_text):
        text=tweet._json["full_text"]
        print(text)
        x=x+1
        username=tweet.user.name
        location=tweet.user.location
        favourite_count = tweet.favorite_count
        retweet_count = tweet.retweet_count
        created_at = tweet.created_at
        line = {'text' : text, 'favourite_count' : favourite_count, 'retweet_count' : retweet_count, 'created_at' : created_at,'username':username,'location' : location}
        output.append(line)
        if(x>20000):
            break
df = pd.DataFrame(output)
df.to_csv('output.csv')