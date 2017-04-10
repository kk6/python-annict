# -*- coding: utf-8 -*-


def pytest_funcarg__api_factory(request):
    class APIFactory:
        def create(self, token='dummy_token'):
            from annict.api import API
            return API(token)
    return APIFactory()
