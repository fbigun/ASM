# -*- coding: utf-8 -*-
import logging
import binascii

import pytest

from asm.utils import Base64decode, ssrParse
from asm.exceptions import SchemesError

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
nh = logging.NullHandler()
nh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
nh.setFormatter(formatter)
logger.addHandler(nh)


@pytest.fixture(scope='module')
def ssr_context():
    with open('tests/resource/ssr.txt', 'r') as f:
        ssr_text = f.read()
    return ssr_text


def test_ssrparser(ssr_context):
    ssrs = Base64decode(ssr_context)
    for ssr in ssrs.split():
        if len(ssr.split('://')) != 2:
            raise SchemesError
        ssrscheme, body = ssr.split('://')
        if ssrscheme == 'ssr':
            try:
                json = ssrParse(body)
            except binascii.Error as e:
                logger.info(body)
                logger.critical(e)
                raise e
            else:
                logger.debug(json)
