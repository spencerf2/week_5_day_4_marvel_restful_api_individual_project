import os
from dotenv import load_dotenv

# Allow outside files/folders to be added to the project from the
# base directory regardless of the operating system.

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    '''Set our config variables'''

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off SQLAlchemy update
                                           # messages