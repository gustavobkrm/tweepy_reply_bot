import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():

    consumer_key = "1fNpziUeJo0oj17cAKikeDIov"
    consumer_secret = "v1GRHgKZQ8bt2ksrTD6rJWnRwmUClWWkGt5GoGb2WE2QXbnfu0"
    access_token = "1036490204088033280-dZ3WAnWUTK9OHMLjJA0EIh0H73iTdS"
    access_token_secret = "kP8NCUsH1UBBpqjbQAjy2RVQEQgavOO1swotnom7mvALO"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api