# -*- coding: utf-8 -*-
import json
from urllib.parse import urljoin

from rauth import OAuth2Service


class OAuthHandler(object):

    def __init__(self, client_id, client_secret, name='annict', base_url='https://api.annict.com',
                 redirect_uri='urn:ietf:wg:oauth:2.0:oob'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.name = name
        self.base_url = base_url
        self.redirect_uri = redirect_uri
        self.auth_session = None
        self.oauth = OAuth2Service(client_id=client_id,
                                   client_secret=client_secret,
                                   name=name,
                                   base_url=base_url,
                                   authorize_url=urljoin(base_url, '/oauth/authorize'),
                                   access_token_url=urljoin(base_url, '/oauth/token'))

    def get_authorization_url(self, scope='read'):
        params = {'scope': scope, 'response_type': 'code', 'redirect_uri': self.redirect_uri}
        return self.oauth.get_authorize_url(**params)

    def authenticate(self, code, decoder=lambda s: json.loads(s.decode('utf8'))):
        data = {'code': code, 'grant_type': 'authorization_code', 'redirect_uri': self.redirect_uri}
        session = self.oauth.get_auth_session(data=data, decoder=decoder)
        self.auth_session = session

    def get_access_token(self):
        if self.auth_session:
            return self.auth_session.access_token
