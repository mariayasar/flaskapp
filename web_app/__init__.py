"""Entry point for the tweeter flask app """

from .app import create_app

APP = create_app()
APP.run(debug=True)