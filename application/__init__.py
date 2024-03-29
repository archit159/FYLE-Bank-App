from flask import Flask
from flask_jwt_extended import JWTManager
import os, sys, json
import logging, logging.handlers
from sqlalchemy.engine.url import URL
import atexit, random, string, datetime

with open(os.path.dirname(__file__) + '/../app-configs/app_config.json') as cfg_file:
    Config = json.load(cfg_file)

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SECRET_KEY'] = Config['secret_key']
application.config['JWT_SECRET_KEY'] = Config['secret_key']
application.config['SQLALCHEMY_POOL_RECYCLE'] = Config['database']['net_read_timeout']

jwt = JWTManager(application)

from application import views
