# -*- coding: utf-8 -*-
import requests
from furl import furl

from .exceptions import AnnictError


class Client(object):

    def __init__(self, access_token, base_url='https://api.annict.com', api_version='v1'):
        self.base_url = base_url
        self.api_version = api_version
        self.session = requests.Session()
        self.session.params['access_token'] = access_token

    def request(self, method, path, params=None):
        """Sends a request"""
        url = furl(self.base_url)
        url.path.add(self.api_version).add(path)
        resp = self.session.request(method, url.url, params=params)

        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 204:
            return True
        elif (resp.status_code // 100) in (4, 5):
            e = resp.json()['errors'][0]
            raise AnnictError(f"{e['type']}:{e['message']}: {e['developer_message']}")
        else:
            return resp
