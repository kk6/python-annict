# -*- coding: utf-8 -*-
from urllib.parse import parse_qs


def test_get_authorization_url():
    from annict.auth import OAuthHandler

    auth = OAuthHandler("dummy_client_id", "dummy_client_secret")
    url = auth.get_authorization_url()
    endpoint, qs = url.split("?")

    assert endpoint == "https://api.annict.com/oauth/authorize"
    assert parse_qs(qs) == {
        "scope": ["read"],
        "client_id": ["dummy_client_id"],
        "redirect_uri": ["urn:ietf:wg:oauth:2.0:oob"],
        "response_type": ["code"],
    }
