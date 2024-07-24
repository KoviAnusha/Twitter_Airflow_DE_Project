import tweepy
import pandas as pd
import s3fs
import json

def run_twitter_etl():

    api_key=""
    api_secret=""
    access_token=""
    access_secret_token=""

    # Initialize OAuth 1.0a User Context
    auth = tweepy.OAuth1UserHandler(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret_token
    )

    api = tweepy.API(auth)
    try:
        user = api.verify_credentials()
        print(user._json)
        user_dict = user._json 
        df = pd.DataFrame([user_dict]) 
    except tweepy.TweepError as e:
        print("Tweepy Error: ", e)

    df.to_csv("/home/anushakovi/airflow_project/twitter_data.csv")

run_twitter_etl()