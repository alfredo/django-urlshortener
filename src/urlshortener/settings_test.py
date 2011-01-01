import os

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/urlshortener.db'
INSTALLED_APPS = ['urlshortener']
ROOT_URLCONF = 'urlshortener.urls'
# urlshortener
URLSHORTENER_EXCLUDE_IPS = []

TEMPLATE_DIRS = os.path.join(os.path.dirname(__file__), 'tests', 'templates')
