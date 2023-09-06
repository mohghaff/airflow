import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
from tweepy.auth import OAuthHandler

def run_twitter_etl():


    consumer_key = "dCmkXvkPz8YsqAQpFkGMnOrdw"
    consumer_secret = "AUsNeGfn8Q3JzbUN1PLO6lGHsWdIrrDGrmY2WfCvCUQJKAAsl1"
    access_token="1699078376043253760-M9dDc1envfiYEclVlKXihTtlpnRU9q"
    access_token_secret="JlBHxZ71ntea86DV0Q9SqNcKOrlxPlH3c5g4iFb0pKdtN"


    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)


    author_ids = ['@kahneman_daniel', '@DAcemogluMIT', '@tegmark', '@George_Friedman', '@harari_yuval', '@sapinker']  

    author_data_list = []

    for id in author_ids:
        user = api.get_user(screen_name=id)
        author_data = {
            'User Name': user.name,
            'User ID': user.id,
            'User Description': user.description,
            'Location': user.location,
            'Followers Count': user.followers_count,
            'Verified': user.verified,
            'Created At': user.created_at
            
        }
        author_data_list.append(author_data)

    author_df = pd.DataFrame(author_data_list)

    author_df.to_csv("s3://mohghaff-twitter-bucket/authors_on_twitter.csv")
