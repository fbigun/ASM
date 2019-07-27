# -*- coding: utf-8 -*-
from asm.utils import Base64decode, Base64encode, urlsafe_base64decode, urlsafe_base64encode, urldecode, urlencode

a = 'M'
A = 'TQ=='

b = 'Ma'
B = 'TWE='

c = 'Man'
C = 'TWFu'

d = '诸多不便'
D = '6K+45aSa5LiN5L6/'
urlD = '6K-45aSa5LiN5L6_'


def judge_encode(func):
    if func(a) == A and func(b) == B and func(c) == C:
        return True
    return False


def judge_decode(func):
    if func(A) == a and func(B) == b and func(C) == c:
        return True
    return False


def test_Base64encode():
    assert judge_encode(Base64encode)


def test_Base64decode():
    assert judge_decode(Base64decode)


def test_urlsafe_base64encode():
    assert judge_encode(urlsafe_base64encode)
    assert urlsafe_base64encode(d) == urlD


def test_urlsafe_base64decode():
    assert judge_decode(urlsafe_base64decode)
    assert urlsafe_base64decode(urlD) == d


def test_urlencode():
    assert urlencode(' ') == '%20'


def test_urldecode():
    assert urldecode('%20') == ' '
