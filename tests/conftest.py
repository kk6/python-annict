# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def api_factory():
    class APIFactory:
        def create(self, token='dummy_token'):
            from annict.api import API
            return API(token)
    return APIFactory()
