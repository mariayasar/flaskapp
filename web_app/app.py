from flask import Flask, escape, request, jsonify, render_template
from decouple import config
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from .models import DB, User, Tweet

def create_app():

    app = Flask(__name__)

    #stop tracking modifications on aqlalchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    #add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    #have the database know about the app
    DB.init_app(app)

    #todo: register routes
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

   
    return app






# To run it: FLASK_APP=web_app flask run