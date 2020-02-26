from flask import Blueprint
home_routes=Blueprint("home_routes", __name__)

 
@home_routes.route('/')
def hello():
    x=4+4
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)},{x}!'

@home_routes.route('/about')
def about():
    return f'About me!'
