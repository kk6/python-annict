# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def dummy_api():
    class DummyAPI:
        base_url = 'https://api.annict.com'
        api_version = 'v1'
        token = 'dummy_token'
    return DummyAPI()


@pytest.mark.parametrize("arg,expected", [
    (1, 'path/to/1'),
    (0, 'path/to/0'),
    ('1', 'path/to/1'),
    (None, 'path/to'),
])
def test_build_path(arg, expected, dummy_api):
    from annict.services import APIMethod

    api_method = APIMethod(api=dummy_api, path='path/to', method='GET')
    api_method.build_path(arg)
    assert api_method.path == expected


def test_build_url(dummy_api):
    from annict.services import APIMethod
    api_method = APIMethod(api=dummy_api, path='path/to', method='GET')
    assert api_method.build_url() == 'https://api.annict.com/v1/path/to'
