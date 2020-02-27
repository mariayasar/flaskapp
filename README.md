# flaskapp
new app


Create DB: 
1. set up models.py with a schema of the  tables 
2. import it into the app.py

3. add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

4.have the database know about the app
    DB.init_app(app)

5. Open Flask shell, create DB (ones)
 DB.create_all() - creates empty DB

6. Import schema from the flask shell: 
    from web_app.models import * 

7. Create fake users 
    u1=User(name='Ma', id=1123)

8. Add entries  to the DB 
    DB.session.add(u1)

9. Commit changes 
    DB.session.commit()


10. If schema changes, then 
DB.drop_all() -- will delete DB

After that, create it again, and populate, commit. 



Twitter commands: 

in flask shell: 
from web_app.twitter import * 
twitter_user=TWITTER.get_user('elonmusk')
tweets=twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, mode='extended)
tweets[0].text #shows the text of the tweet 




Basilica
embedding=BASILICA.embed_sentence(tweet_text, model='twitter')


#Add tweets to the DB: 
for tweet in tweets:
embedding=BASILICA.embed_sentence(tweet.full_text, model='twitter')
db_tweet=Tweet(id=tweet.id, text=tweet.full_text[:500], embedding=embedding)
DB.session.add(db_tweet)
db_user.tweets.append(db_tweet)