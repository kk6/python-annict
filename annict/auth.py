# -*- coding: utf-8 -*-
import json
from urllib.parse import urljoin
import webbrowser

from rauth import OAuth2Service


class AnnictOAuthHandler(object):
    NAME = 'annict'
    BASE_URL = 'https://api.annict.com'

    def __init__(self, client_id, client_secret, redirect_uri='urn:ietf:wg:oauth:2.0:oob'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.oauth = None

    def authorize(self, scope='read'):
        authorize_url = urljoin(self.BASE_URL, '/oauth/authorize')
        access_token_url = urljoin(self.BASE_URL, '/oauth/token')
        self.oauth = OAuth2Service(client_id=self.client_id, client_secret=self.client_secret,
                                   authorize_url=authorize_url, base_url=self.BASE_URL, name=self.NAME,
                                   access_token_url=access_token_url)
        params = {'scope': scope, 'response_type': 'code', 'redirect_uri': self.redirect_uri}
        authorize_url = self.oauth.get_authorize_url(**params)
        return webbrowser.open(authorize_url)

    def authenticate(self, code, decoder=lambda s: json.loads(s.decode('utf8'))):
        data = {'code': code, 'grant_type': 'authorization_code', 'redirect_uri': self.redirect_uri}
        return self.oauth.get_auth_session(data=data, decoder=decoder)
