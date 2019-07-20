# -*- coding: utf-8 -*-
"""
WSGI config for gettingstarted project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

from app import app

application = app

if __name__ == '__main__':
    application.run(host='127.0.0.1', port=8080)
