import os

from flask import Flask
from twx.botapi import TelegramBot
from flask_sqlalchemy import SQLAlchemy

bot_api_key = os.environ.get('TELEGRAM_BOT_APIKEY')

bot = TelegramBot(bot_api_key)

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(application)

from app import views
from app import models

if os.environ.get('HEROKU') is not None:
    import logging

    stream_handler = logging.StreamHandler()
    application.logger.addHandler(stream_handler)
    application.logger.setLevel(logging.DEBUG)

with application.app_context():
    db.create_all()
