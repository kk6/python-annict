# -*- coding: utf-8 -*-
from .models import MODEL_MAPPING


class ModelParser(object):
    def __init__(self, api, model_mapping=None):
        self.model_mapping = model_mapping if model_mapping else MODEL_MAPPING
        self._api = api

    def parse(self, json, payload_type, payload_is_list=False):
        model = self.model_mapping[payload_type]
        if payload_is_list:
            return model.parse_list(self._api, json, payload_type)
        else:
            return model.parse(self._api, json)
