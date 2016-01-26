# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# mail server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('e.paguntalan')
MAIL_PASSWORD = os.environ.get('12354667890')

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

# administrator list
ADMINS = ['e.paguntalan@klab.com']

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = 'lele' # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = 'aGlS43GFMEYidS1SMHQ6wrYZnxYgFWGgyZWYiJx/7dA=' # enter your MS translator app secret here

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50
