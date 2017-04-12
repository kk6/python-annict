# -*- coding: utf-8 -*-
from furl import furl
import requests

from .utils import stringify


class APIMethod(object):

    def __init__(self, api, path, method, allowed_params=None, payload_type=None, payload_list=False):
        self.api = api
        self.path = path
        self.method = method
        self.allowed_params = allowed_params
        self.payload_type = payload_type
        self.payload_list = payload_list

    def build_path(self, id_=None):
        if id_ is not None:
            self.path = '/'.join([self.path, str(id_)])

    def build_url(self):
        url = furl(self.api.base_url)
        url.path.add(self.api.api_version).add(self.path)
        return url.url

    def build_parameters(self, dic):
        params = {key: stringify(dic[key]) for key in self.allowed_params if key in dic and dic[key]}
        params['access_token'] = self.api.token
        return params

    def __call__(self, params):
        url = self.build_url()
        resp = requests.request(self.method, url, params=params)

        resp.raise_for_status()

        if resp.status_code == 200:
            return self.api.parser.parse(resp.json(), self.payload_type, self.payload_list)
        elif resp.status_code == 204:
            return True
        else:
            return resp
