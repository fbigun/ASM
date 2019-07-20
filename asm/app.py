# -*- coding: utf-8 -*-
from bottle import Bottle

app = Bottle()


@app.route('/')
def hello():
    return 'Hello World!'
