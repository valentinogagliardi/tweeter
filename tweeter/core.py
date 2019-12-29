import tweepy
from typing import Dict
from tweeter.exceptions import NotConfiguredError


class Tweeter:
    def __init__(self, config: Dict):
        if not config:
            raise NotConfiguredError("Expected a configuration dict, found none")
        consumer_key = config.get("consumer_key", None)
        consumer_secret = config.get("consumer_secret", None)
        access_token = config.get("access_token", None)
        access_token_secret = config.get("access_token_secret", None)
        auth = tweepy.OAuthHandler(
            consumer_key=consumer_key, consumer_secret=consumer_secret
        )
        auth.set_access_token(key=access_token, secret=access_token_secret)
        self.api = tweepy.API(auth)

    def _build_tweet(self):
        raise NotImplementedError

    def post_tweet(self):
        tweet = self._build_tweet()
        try:
            self.api.update_status(tweet)
        except tweepy.TweepError as err:
            if err.api_code == 187:
                print("Duplicate tweet, discarding")
