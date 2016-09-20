import os
import sys
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Cursor

def get_twitter_auth():
    try:
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_secret = os.environ['TWITTER_ACCESS_SECRET']
        # consumer_key="856XqlISqQ8Noy6ucm95zOMQA"
        # consumer_secret="nHCfJhQj2byDzKGcXiVQnr1RiTAFDHTpPTLqx91JMMhuFwCzpO"
        # access_token="765900228423811072-D7bnh4T1lLDTD8uZofAU4ogwHrFJizH"
        # access_secret="xD1QFtkjXx7xldRfD9qiWGkJVA4QWuTajt3D1wCCUhYny"
    except KeyError:
        sys.stderr.write("Twitter environment variable not set.\n")
        sys.exit(1)
    auth=OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth=get_twitter_auth()
    client=API(auth)
    # print(auth.get_username())
    return client

if __name__=='__main__':
    client=get_twitter_client()
    for status in Cursor(client.home_timeline).items(10):
        print(status.text)


