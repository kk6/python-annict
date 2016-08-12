# -*- coding: utf-8 -*-
from operator import methodcaller

import requests
from furl import furl


class Client(object):

    def __init__(self, access_token, base_url='https://api.annict.com', api_version='v1'):
        self.access_token = access_token
        self.base_url = base_url
        self.api_version = api_version

    def _request(self, http_method, path, kwargs=None):
        kwargs['access_token'] = self.access_token

        d = {}
        if http_method == 'post' or http_method == 'patch':
            d['data'] = kwargs
        elif http_method == 'get':
            d['params'] = kwargs

        url = furl(self.base_url)
        url.path.add(self.api_version).add(path)
        m = methodcaller(http_method, url.url, **d)
        response = m(requests)

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
