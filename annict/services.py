# -*- coding: utf-8 -*-
from .exceptions import AnnictError
from .utils import stringify


class APIMethod(object):

    def __init__(self, api, path, method, required_params, optional_params, target_id=None):
        self.api = api
        self.path = path
        self.method = method
        self.allowed_params = required_params + optional_params
        self.target_id = target_id

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

    def __call__(self, *args, **kwargs):
        self.build_path()
        params = self.build_parameters(args, kwargs)
        client_method = getattr(self.api.client, self.method.lower())
        return client_method(self.path, params)
