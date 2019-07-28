# -*- coding: utf-8 -*-
from binascii import Error


class BaseError(Error):
    """一个模棱两可的异常"""


class Base64Error(BaseError):
    """base64 编码解码异常"""


class EnvError(BaseError):
    """环境变量未设置或设置错误"""


class SchemesError(BaseError):
    """连接协议不支持"""
