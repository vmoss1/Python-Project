import os

class Configuration(object):
    SECRET_KEY=os.environ.get('SECRET_TUNNEL')
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
