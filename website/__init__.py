from flask import Flask
import os

x = os.urandom(12)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = x

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app