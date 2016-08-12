# -*- coding: utf-8 -*-
from operator import methodcaller

import requests


class Client(object):

    def __init__(self, access_token, base_url='https://api.annict.com', api_version='v1'):
        self.access_token = access_token
        self.base_url = base_url
        self.api_version = api_version

    def _request(self, method, path, kwargs=None):
        url = '/'.join([self.base_url, self.api_version, path])
        kwargs['access_token'] = self.access_token

        d = {}
        if method == 'post' or method == 'patch':
            d['data'] = kwargs
        elif method == 'get':
            d['params'] = kwargs
        f = methodcaller(method, url, **d)
        response = f(requests)

        if not response.content:
            return None

        return response.json()

    def get(self, path, kwargs):
        return self._request('get', path, kwargs)

    def post(self, path, kwargs):
        return self._request('post', path, kwargs)

    def patch(self, path, kwargs):
        return self._request('patch', path, kwargs)

    def delete(self, path):
        return self._request('delete', path)
