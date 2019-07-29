# -*- coding: utf-8 -*-
from base64 import b64decode, b64encode, urlsafe_b64decode, urlsafe_b64encode
from urllib.parse import quote, unquote
from functools import partial

from .exceptions import Base64Error, SsrParserError, codeError


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


def ssrParse(uri):
    ssr_uri = urlsafe_base64decode(uri)

    if ':' not in ssr_uri:
        raise SsrParserError
    elif '/?' not in ssr_uri:
        if len(ssr_uri.split(':') != 6):
            raise SsrParserError
        base_server_info = ssr_uri.split(':')
    elif len(ssr_uri.split('/?')) != 2:
        raise SsrParserError
    else:
        base_server_info = ssr_uri.split('/?')[0].split(':')

    base_server_info[-1] = urlsafe_b64decode(base_server_info[-1])
    server, server_port, proto, method, obfs, passwd = base_server_info

    data = {
        'server': server,
        'server_port': server_port,
        'proto': proto,
        'method': method,
        'obfs': obfs,
        'passwd': passwd
    }

    for i in ssr_uri.split('/?')[1].split('&'):
        k = i.split('=')[0]
        v = urlsafe_base64decode(i.split('=')[1])
        if k in ['obfsparam', 'protoparam', 'group']:
            data[k] = v
        elif k == 'remarks':
            data['name'] = v
        else:
            raise SsrParserError('不支持更多参数{}'.format(k))

    if not (server and server_port and proto and method and passwd and obfs):
        raise SsrParserError

    return data
