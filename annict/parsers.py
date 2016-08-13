# -*- coding: utf-8 -*-
from .models import MODEL_MAPPING


class ModelPerser(object):
    def __init__(self, api):
        self.model_mapping = MODEL_MAPPING
        self._api = api

    def parse(self, json, payload_type):
        model = self.model_mapping[payload_type]
        return model.parse_list(self._api, json, payload_type)
