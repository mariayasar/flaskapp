from flask import Flask, escape, request, jsonify, render_template
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from .models import DB

def create_app():

    app = Flask(__name__)
    
    #add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    #have the database know about the app
    DB.init_app(app)

    #todo: register routes
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

   
    return app






# To run it: FLASK_APP=web_app flask run