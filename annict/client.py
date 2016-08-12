# -*- coding: utf-8 -*-
from operator import methodcaller

import requests
from furl import furl


class Client(object):

    def __init__(self, access_token, base_url='https://api.annict.com', api_version='v1'):
        self.access_token = access_token
        self.base_url = base_url
        self.api_version = api_version
        self._furl = furl(base_url)
        self._furl.path.add(api_version)

    def _request(self, method, path, kwargs=None):
        self._furl.path.add(path)
        kwargs['access_token'] = self.access_token

        d = {}
        if method == 'post' or method == 'patch':
            d['data'] = kwargs
        elif method == 'get':
            d['params'] = kwargs
        f = methodcaller(method, self._furl.url, **d)
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
