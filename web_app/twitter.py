"""Retrieve tweets, embedding, save into database"""

import basilica
import tweepy
from decouple import config
from .models import DB, Tweet, User
import json

TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'), config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA=basilica.Connection(config('BASILICA_KEY'))


#Add tweets to the DB: 
def add_tweets_to_db(tweets):
    """Function that writes tweets into the database """
    # db_user=User(name='', newest_tweet_id=tweets[0].id)
    # DB.session.add(db_user)

    #db_user.tweets.append(db_tweet)
    for tweet in tweets:
       
        embedding = BASILICA.embed_sentence(tweet.text, model='twitter')
        db_tweet=Tweet(id=tweet.id, text=tweet.text[:500], user_id=tweet.user.id, embedding=embedding)
        # DB.session.add(db_tweet)
        
        # print(db_tweet.id, db_tweet.text)
    # DB.session.commit()
   


def foobar(username):
    """Function that connects to Twitter API and pulls last 200 tweets from the username"""
  # public_tweets = TWITTER.home_timeline()
    user = TWITTER.get_user(username)
    tweets=user.timeline(count=200, exclude_replies=True, include_rts=False, mode='extended')
    #profile_image_url=tweets[0].profile_image_url
    
    #insert user in the database
    user_db=User(id=tweets[0].user.id, name=tweets[0].user.name, newest_tweet_id=tweets[0].id)
    DB.session.add(user_db)
    DB.session.commit()
    
    #insert tweets in the database
    for tweet in tweets:
        embedding = BASILICA.embed_sentence(tweet.text, model='twitter')
        db_tweet=Tweet(id=tweet.id, text=tweet.text[:500], user_id=tweet.user.id, embedding=embedding)
        DB.session.add(db_tweet)
    DB.session.commit()

    return user, tweets


  
#to do - add functions later