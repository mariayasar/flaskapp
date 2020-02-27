from flask import Blueprint, render_template, request, jsonify
home_routes=Blueprint("home_routes", __name__)
from web_app.models import DB, User, Tweet
import web_app.twitter
from flask_sqlalchemy import SQLAlchemy
from web_app.predict import predict_user
 
@home_routes.route('/')
def hello():

    users = User.query.all()
    return render_template('base.html', title='Maria', users=users)

@home_routes.route('/about')
def about():
    return render_template("about.html")

@home_routes.route('/reset')
def reset():
    DB.drop_all()
    DB.create_all()
    return render_template('base.html', title='Reset', users=[])

#Route to download tweets from our local DB,  show on the page
@home_routes.route('/user/<path:u_path>')
def catch_all(u_path):
    #user, tweets=web_app.twitter.foobar(u_path)
    user = User.query.filter_by(name=u_path).first()
    tweets  = Tweet.query.filter_by(user_id=user.id).all()
    return render_template('user_page.html', user=user, tweets=tweets)


@home_routes.route('/user/select')
def select_user(): 
    return render_template('select_user.html')


@home_routes.route('/user', methods=["POST", "GET"])
def get_user_data():

    username=request.form['name']
    user, tweets=web_app.twitter.foobar(username)
    #web_app.twitter.add_tweets_to_db(tweets)

    return render_template('user_page.html', user=user, tweets=tweets)



@home_routes.route('/predict', methods=["POST"])
def predict(message=''):
    user1, user2 = sorted([request.values['handle1'], request.values['handle2']])
    if user1 == user2: 
        message = 'Cannot compare a user to themselves!'
    else: 
        prediction = predict_user(user1, user2, request.form['new_tweet'])
        message='"{}" is more likely to be said by {} than {}'.format(request.values['new_tweet'], user1 if prediction else user2,
            user2 if prediction else user1)

    return render_template('prediction.html', title='Prediction', message=message)



# @book_routes.route('/books/new')
# def new_book():
#     return render_template("new_book.html")

# @book_routes.route('/books/create', methods=["POST"])
# def create_book():
        
#     print("FORM DATA:", dict(request.form))
#     #todo: store data in the db
#     return jsonify({"message": "BOOK CREATED OK"})



# @home_routes.route('/user/elon')
# def user():
#     tweets  = Tweet.query.filter_by(user_id=44196397).all()
#     return render_template('user.html', tweets=tweets)

# @home_routes.route('/user/<path:u_path>')
# def catch_all(u_path):
#     print(repr(u_path))
#     web_app.twitter.foobar()
#     user = User.query.filter_by(name=u_path).first()
#     tweets  = Tweet.query.filter_by(user_id=user.id).all()
#     return render_template('user.html', tweets=tweets)


# #Route to download tweets from Twitter, upload them into DB
# Commenting this out -- will duplicate, but pulling data from the database instead
# @home_routes.route('/user/<path:u_path>')
# def catch_all(u_path):
#     user, tweets=web_app.twitter.foobar(u_path)
#     #user = User.query.filter_by(name=u_path).first()
#     #tweets  = Tweet.query.filter_by(user_id=user.id).all()
#     return render_template('user_page.html', user=user, tweets=tweets)
