import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    ''' Configuration for the Flask application '''
    APP_ROOT = APP_ROOT
    # To set up debug mode
    DEBUG = True
    # To set up testing mode
    TESTING = True
    # Database to use with SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + APP_ROOT + '/website.db'
    # Secret key for session signing
    SECRET_KEY = 'ThisIsMySecretKeyForThisApplication'