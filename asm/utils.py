# -*- coding: utf-8 -*-
from base64 import b64decode, b64encode, urlsafe_b64decode, urlsafe_b64encode
from urllib.parse import quote, unquote
from functools import partial

from .exceptions import Base64Error, codeError


def Base64encode(text, method=b64encode):
    base64Str = method(text.encode()).decode()

    return base64Str


def Base64decode(base64Str, method=b64decode):
    if not isinstance(base64Str, str):
        raise codeError

    # base64 decode should meet the padding rules
    s_padding = ''
    n = len(base64Str) % 4

    if n == 1:
        raise Base64Error('非法字符串,不是一个可解码的字符串')
    elif n == 2:
        s_padding = '=='
    elif n == 3:
        s_padding = '='
    base64Str_padding = base64Str + s_padding

    text = method(base64Str_padding.encode()).decode()

    return text


urlsafe_base64decode = partial(Base64decode, method=urlsafe_b64decode)
urlsafe_base64encode = partial(Base64encode, method=urlsafe_b64encode)


def urlencode(text):
    return quote(text)


def urldecode(urlStr):
    return unquote(urlStr)
