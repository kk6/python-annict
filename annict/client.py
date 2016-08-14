# -*- coding: utf-8 -*-
import requests
from furl import furl


class Client(object):

    def __init__(self, access_token, base_url='https://api.annict.com', api_version='v1'):
        self.access_token = access_token
        self.base_url = base_url
        self.api_version = api_version

    def _request(self, method, path, params=None):
        params['access_token'] = self.access_token

        kwargs = {}
        if method == 'post' or method == 'patch':
            kwargs['data'] = params
        elif method == 'get':
            kwargs['params'] = params

        url = furl(self.base_url)
        url.path.add(self.api_version).add(path)
        resp = requests.request(method, url.url, **kwargs)

        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 204:
            return True
        else:
            return resp

    def get(self, path, params):
        return self._request('get', path, params)

    def post(self, path, params):
        return self._request('post', path, params)

    def patch(self, path, params):
        return self._request('patch', path, params)

    def delete(self, path):
        return self._request('delete', path)
