# -*- coding: utf-8 -*-
import typing
from typing import Any
from typing import Optional
from typing import Tuple

import requests
from furl import furl

from .utils import stringify

if typing.TYPE_CHECKING:
    from .api import API


class APIMethod(object):
    """A class abstracting each method of AnnictAPI

    :param api: instance of :class:`API <annict.api.API>` .
    :type api: annict.api.API
    :param str path: Endpoint path
    :param str method: HTTP Method
    :param tuple allowed_params: (optional) List of request parameter names that can be sent.
    :param str payload_type: Type of payload
    :param bool payload_list: Specifies whether the payload is a list or not.

    """

    def __init__(
        self,
        api,
        path,
        method,
        allowed_params=None,
        payload_type=None,
        payload_is_list=False,
    ) -> None:
        self.api: API = api
        self.path: str = path
        self.method: str = method
        self.allowed_params: Tuple[Optional[str]] = allowed_params
        self.payload_type: str = payload_type
        self.payload_is_list: bool = payload_is_list

    def build_path(self, id_: int = None) -> None:
        """Build an suitable path

        If `id_` is given, it is embedded into path.

        :param int id_: Target resource ID

        """
        if id_ is not None:
            self.path = "/".join([self.path, str(id_)])

    def build_url(self) -> str:
        """Build request url

        :return: request url
        :rtype: str

        """
        url = furl(self.api.base_url)
        url.path.add(self.api.api_version).add(self.path)
        return url.url

    def build_parameters(self, dic: dict) -> dict:
        """Build a suitable parameters for request.

        It filters the given dictionary based on `self.allowed_params` and returns a dictionary with
        an additional access token.

        :param dict dic: dict of arguments given to annict.API's method.
        :return: dict for request parameter
        :rtype: dict

        """
        params = {
            key: stringify(dic[key])
            for key in self.allowed_params
            if key in dic and dic[key]
        }
        params["access_token"] = self.api.token
        return params

    def __call__(self, params) -> Any:
        url = self.build_url()
        resp = requests.request(self.method, url, params=params)

        resp.raise_for_status()

        if resp.status_code == 200:
            return self.api.parser.parse(
                resp.json(), self.payload_type, self.payload_is_list
            )
        elif resp.status_code == 204:
            return True
        else:
            return resp
