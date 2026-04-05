import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SECRET_KEY = 'MY_SECRET_KEY'
    DROPBOX_TOKEN = os.getenv('DROPBOX_TOKEN')
