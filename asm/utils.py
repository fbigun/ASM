# -*- coding: utf-8 -*-
from base64 import urlsafe_b64decode, urlsafe_b64encode
from urllib.parse import quote, unquote


def Base64encode(text):
    base64Str = urlsafe_b64encode(text.encode()).decode()

    return base64Str


def Base64decode(base64Str):
    # base64 decode should meet the padding rules
    s_padding = ''
    n = len(base64Str) % 3

    if n == 1:
        s_padding = '=='
    elif n == 2:
        s_padding = '='
    base64Str_padding = base64Str + s_padding

    text = urlsafe_b64decode(base64Str_padding.encode()).decode()

    return text


def urlencode(text):
    return quote(text)


def urldecode(text):
    return unquote(text)
