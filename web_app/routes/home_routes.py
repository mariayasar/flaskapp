from flask import Blueprint, render_template
home_routes=Blueprint("home_routes", __name__)

 
@home_routes.route('/')
def hello():
    x=4+4
    return f'Hello, World {x}'

@home_routes.route('/about')
def about():
    return render_template("about.html")
