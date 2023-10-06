from flask import Flask
from .data_api import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

