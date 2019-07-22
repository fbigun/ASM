# -*- coding: utf-8 -*-
from base64 import b64decode, b64encode, urlsafe_b64decode, urlsafe_b64encode
from urllib.parse import quote, unquote
from functools import partial


def Base64encode(text, method=b64encode):
    base64Str = method(text.encode()).decode()

    return base64Str


def Base64decode(base64Str, method=b64decode):
    # base64 decode should meet the padding rules
    s_padding = ''
    n = len(base64Str) % 3

    if n == 1:
        s_padding = '=='
    elif n == 2:
        s_padding = '='
    base64Str_padding = base64Str + s_padding
    print(base64Str_padding)

    text = method(base64Str_padding.encode()).decode()

    return text


urlsafe_base64decode = partial(Base64decode, method=urlsafe_b64decode)
urlsafe_base64encode = partial(Base64encode, method=urlsafe_b64encode)


def urlencode(text):
    return quote(text)


def urldecode(text):
    return unquote(text)
