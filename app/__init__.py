from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ
from flask_login import LoginManager, UserMixin

# Attempt to import Database URI and secret key
DATABASE_URI = environ.get('APP_DATABASE_URI')
SECRET_KEY = environ.get('APP_SECRET_KEY')
if DATABASE_URI == None or SECRET_KEY == None:
    raise ValueError('Environment variables not set')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY
app.config['TESTING'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

from app import views