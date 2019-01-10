# -*- coding: utf-8 -*-


class DummyModel(object):
    @classmethod
    def parse(cls, api, json):
        return "Model.parse is called."

    @classmethod
    def parse_list(cls, api, json, payload_type):
        return "Model.parse_list is called."


def test_called_parse():
    from annict.parsers import ModelParser

    model_mapping = {"model": DummyModel}
    parser = ModelParser("api", model_mapping)
    json = {}
    r = parser.parse(json, "model")
    assert r == "Model.parse is called."


def test_called_parse_list():
    from annict.parsers import ModelParser

    model_mapping = {"model": DummyModel}
    parser = ModelParser("api", model_mapping)
    json = {"total_count": 100}
    r = parser.parse(json, "model", payload_is_list=True)
    assert r == "Model.parse_list is called."
