# -*- coding: utf-8 -*-
import requests


class Client(object):

    def __init__(self, access_token, base_url='https://api.annict.com', api_version='v1'):
        self.access_token = access_token
        self.base_url = base_url
        self.api_version = api_version

    def _request(self, method, path, **kwargs):
        url = '/'.join([self.base_url, self.api_version, path])
        kwargs['access_token'] = self.access_token

        method = method.lower()
        if method == 'get':
            response = requests.get(url, params=kwargs)
        elif method == 'post':
            response = requests.post(url, data=kwargs)
        elif method == 'patch':
            response = requests.patch(url, data=kwargs)
        elif method == 'delete':
            response = requests.delete(url)
        else:
            raise ValueError('Unknown HTTP method.')

        if not response.content:
            return None

        return response.json()

    def get(self, path, **kwargs):
        return self._request('GET', path, **kwargs)

    def post(self, path, **kwargs):
        return self._request('POST', path, **kwargs)

    def patch(self, path, **kwargs):
        return self._request('PATCH', path, **kwargs)

    def delete(self, path, **kwargs):
        return self._request('DELETE', path, **kwargs)
