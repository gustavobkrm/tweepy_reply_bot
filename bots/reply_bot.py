#!/usr/bin/env python
# tweepy-bots/bots/reply_bot.py
import tweepy
import logging
from config import create_api
import time
import random
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def return_random_image():
    path = './'
    imgList = os.listdir(path)
    return imgList

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            media = api.media_upload(filename = random.choice(return_random_image()))
            mid = media.media_id
            api.update_status(status = ("@" + tweet.user.screen_name), in_reply_to_status_id = tweet.id, media_ids = [mid], auto_populate_reply_metadata = True)

    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["caraio"], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()