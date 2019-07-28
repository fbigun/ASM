# -*- coding: utf-8 -*-
import os

from .exceptions import EnvError, SchemesError

PLATFORM = os.environ.get('PLATFORM')
if PLATFORM == 'heroku':
    DATABASE_URL = os.environ['DATABASE_URL']

elif PLATFORM == 'test':
    DATABASE_URL = 'sqlite:///:memory:'

elif PLATFORM == 'develop':
    DATABASE_URL = 'sqlite:///develop.db'

else:
    if os.environ.get('DATABASE_URL'):
        DATABASE_URL = os.environ['DATABASE_URL']
    else:
        DB_TYPE = os.environ.get('DB_TYPE')
        DB_HOST = os.environ.get('DB_HOST')
        DB_NAME = os.environ.get('DB_NAME')
        DB_PORT = os.environ.get('DB_PORT')
        DB_USER = os.environ.get('DB_USER')
        DB_PASSWD = os.environ.get('DB_PASSWD')
        if DB_TYPE == 'sqlite' and DB_NAME:
            DATABASE_URL = 'sqlite:///' + DB_NAME
        elif DB_TYPE and DB_HOST and DB_NAME and DB_PORT and DB_USER and DB_PASSWD:
            DATABASE_URL = DB_TYPE + '://' + DB_USER + ':' + DB_PASSWD + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_NAME
        else:
            raise EnvError

schemes = [
    'mysql',
    'mysql+pool',
    'postgres',
    'postgresql',
    'postgres+pool',
    'postgresql+pool',
    'sqlite',
    'sqliteext',
    'sqlite+pool',
    'sqliteext+pool',
]

scheme = DATABASE_URL.split('://')[0]
url_body = DATABASE_URL.split('://')[1]
if schemes == 'postgresql':
    DATABASE_URL = 'postgre+pool://' + url_body
elif scheme not in schemes:
    raise SchemesError('不支持{}协议'.format(scheme))
