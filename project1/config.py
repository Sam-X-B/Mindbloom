import os
from secrets import token_hex

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'replace-with-a-secure-random-key') or token_hex(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///mindbloom.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.environ.get('FLASK_DEBUG', '0').lower() in ('1', 'true')
    WTF_CSRF_CHECK_DEFAULT = False