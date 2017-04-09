# -*- coding: utf-8 -*-
from furl import furl
import requests

from .exceptions import AnnictError
from .utils import stringify


class APIMethod(object):

    def __init__(self, api, path, method, required_params, optional_params, target_id=None,
                 payload_type=None, payload_list=False):
        self.api = api
        self.path = path
        self.method = method
        self.allowed_params = required_params + optional_params
        self.target_id = target_id
        self.session = requests.Session()
        self.session.params['access_token'] = self.api.token
        self.payload_type = payload_type
        self.payload_list = payload_list

    def build_parameters(self, args, kwargs):
        params = {}
        for i, arg in enumerate(args):
            if arg is None:
                continue
            try:
                params[self.allowed_params[i]] = stringify(arg)
            except IndexError:
                raise AnnictError("Too many parameters supplied.")

        for k, arg in kwargs.items():
            if arg is None:
                continue
            if k in params:
                raise AnnictError(f"Multiple values for parameter '{k}' supplied.")
            if k not in self.allowed_params:
                raise AnnictError(f"Unknown keyword supplied: '{k}'")

            params[k] = stringify(arg)

        return params

    def build_path(self):
        if self.target_id:
            self.path = '/'.join([self.path, str(self.target_id)])

    def build_url(self):
        self.build_path()
        url = furl(self.api.base_url)
        url.path.add(self.api.api_version).add(self.path)
        return url.url

    def __call__(self, *args, **kwargs):
        url = self.build_url()
        params = self.build_parameters(args, kwargs)
        resp = self.session.request(self.method, url, params=params)

        resp.raise_for_status()

        if resp.status_code == 200:
            return self.api.parser.parse(resp.json(), self.payload_type, self.payload_list)
        elif resp.status_code == 204:
            return True
        else:
            return resp
