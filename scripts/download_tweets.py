#!/usr/bin/env python
# encoding: utf-8

import json
import tweepy  # https://github.com/tweepy/tweepy
from dotenv import load_dotenv
import os
import tqdm

from tweepy.models import List

# Twitter API credentials
load_dotenv()

API_KEY = os.environ["API_KEY"]
API_KEY_SECRET = os.environ["API_KEY_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]


def get_all_tweets():
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # find the newest tweet already stored
    newest = 0

    with open("tweets.json") as fp:
        for line in fp:
            newest = max(newest, json.loads(line)['id'])

    # keep grabbing tweets until there are no tweets left to grab
    with open(f"tweets.json", "a") as f:
        # find newest tweets        
        print(f"Getting tweets since {newest}")

        for tweet in tqdm.tqdm(tweepy.Cursor(api.user_timeline, since_id=newest or None).items(), unit=" tweet"):
            f.write(json.dumps(tweet._json) + "\n")


if __name__ == "__main__":
    get_all_tweets()
