# -*- coding: utf-8 -*-
from operator import methodcaller

import requests
from furl import furl


class Client(object):

    def __init__(self, access_token, base_url='https://api.annict.com', api_version='v1'):
        self.access_token = access_token
        self.base_url = base_url
        self.api_version = api_version

    def _request(self, http_method, path, params=None):
        params['access_token'] = self.access_token

        kwargs = {}
        if http_method == 'post' or http_method == 'patch':
            kwargs['data'] = params
        elif http_method == 'get':
            kwargs['params'] = params

        url = furl(self.base_url)
        url.path.add(self.api_version).add(path)
        m = methodcaller(http_method, url.url, **kwargs)
        return m(requests)

    def get(self, path, params):
        return self._request('get', path, params)

    def post(self, path, params):
        return self._request('post', path, params)

    def patch(self, path, params):
        return self._request('patch', path, params)

    def delete(self, path):
        return self._request('delete', path)
