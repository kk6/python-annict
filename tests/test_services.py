# -*- coding: utf-8 -*-


def test_build_parameters():
    from annict.services import ServiceBase

    sb = ServiceBase(None, None)
    sb.allowed_params = ['a', 'b', 'c']
    params = sb.build_parameters({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    assert params == {'a': '1', 'b': '2', 'c': '3'}

