import tweepy
import pandas as pd
import json

def run_twitter_etl():

    # Input keys here
    access_key=""
    access_secret=""
    consumer_key=""
    consumer_secret=""


    # Twitter Authentication
    auth=tweepy.OAuthHandler(access_key,access_secret)
    auth.set_access_token(consumer_key,consumer_secret)

    # Creating API object
    api=tweepy.API(auth)

    # Username and parameters
    tweets=api.user_timeline(screen_name="twitterusername",
                                count=200,
                                include_rts=False,
                                tweet_mode='extended')
                        
    # Appending info to list
    tweet_list=[]
    for tweet in tweet_list:
        text=tweet._json["full_text"]
        refined_tweet = {"user":tweet.user.screen_name,
                        "text":text,
                        "favorite_count":tweet.favorite_count,
                        "retweet_count": tweet.retweet.count,
                        "create_at": tweet.created_at}
        tweet_list.append(refined_tweet)

# Exporting data to s3
    df=pd.DataFrame(tweet_list)
    df.to_csv("s3://airflow-bucket/twitterdata.csv")