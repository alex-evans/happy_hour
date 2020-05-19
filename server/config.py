
import os
from dotenv import load_dotenv

basedir = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(basedir)


class Config:
    '''Set Flask configuration variables from .env file'''

    # General Flask Config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_APP = 'main.py'
    FLASK_DEBUG = 1

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
