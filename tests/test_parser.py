# -*- coding: utf-8 -*-


class DummyResponse:
    """Mock of requests.Response"""
    def __init__(self, json):
        self._json = json

    def json(self):
        return self._json


class DummyModel(object):
    @classmethod
    def parse(cls, api, json):
        return 'Model.parse is called.'

    @classmethod
    def parse_list(cls, api, json, payload_type):
        return 'Model.parse_list is called.'


def test_called_parse():
    from annict.parsers import ModelParser
    model_mapping = {'model': DummyModel}
    parser = ModelParser('api', model_mapping)
    resp = DummyResponse({})
    r = parser.parse(resp, 'model')
    assert r == 'Model.parse is called.'


def test_called_parse_list():
    from annict.parsers import ModelParser
    model_mapping = {'model': DummyModel}
    parser = ModelParser('api', model_mapping)
    resp = DummyResponse({'total_count': 100})
    r = parser.parse(resp, 'model', payload_list=True)
    assert r == 'Model.parse_list is called.'
