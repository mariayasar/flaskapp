"""Retrieve tweets, embedding, save into database"""

import basilica
import tweepy
from decouple import config
from .models import DB, Tweet, User
import json

TWITTER_AUTH = tweepy.OAuthHandler(
    config('TWITTER_CONSUMER_KEY'), config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(
    config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(config('BASILICA_KEY'))
()


def foobar(username):
    """Function that connects to Twitter API and pulls last 200 tweets
    from the username, adds to the database. Will throw error if the
    user does not exist, or is private"""
    try:
        user = TWITTER.get_user(username)
        user_db = (User.query.get(user.id) or User(id=user.id, name=username))
        DB.session.add(user_db)

        tweets = user.timeline(count=200, exclude_replies=True, include_rts=False,
                               mode='extended', since_id=user_db.newest_tweet_id)
        if tweets:
            user_db.newest_tweet_id = tweets[0].id

        for tweet in tweets:
            embedding = BASILICA.embed_sentence(tweet.text, model='twitter')
            db_tweet = Tweet(
                id=tweet.id, text=tweet.text,
                user_id=tweet.user.id, embedding=embedding)
            DB.session.add(db_tweet)
        # profile_image_url=tweets[0].profile_image_url
        DB.session.commit()
        return user, tweets
    except Exception as e:
        print(f'Encountered error while processing {username}: {e} ')
        raise e
    else:
        DB.session.commit()
# to do - add functions later





# # Add tweets to the DB:
# def add_tweets_to_db(tweets):
#     """Function that writes tweets into the database """
#     # db_user=User(name='', newest_tweet_id=tweets[0].id)
#     # DB.session.add(db_user)

#     # db_user.tweets.append(db_tweet)
#     for tweet in tweets:

#         embedding = BASILICA.embed_sentence(tweet.text, model='twitter')
#         db_tweet = Tweet(
#             id=tweet.id, text=tweet.text[:500], user_id=tweet.user.id, embedding=embedding)
#         # DB.session.add(db_tweet)

#         # print(db_tweet.id, db_tweet.text)
#     # DB.session.commit