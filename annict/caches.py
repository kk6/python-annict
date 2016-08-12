# -*- coding: utf-8 -*-
import requests_cache


def install(cache_name='annict_cache', backend='memory', expire_after=300, *args, **kwargs):
    return requests_cache.install_cache(cache_name=cache_name, backend=backend, expire_after=expire_after,
                                        *args, **kwargs)


def uninstall():
    return requests_cache.uninstall_cache()


def enabled(*args, **kwargs):
    return requests_cache.enabled(*args, **kwargs)


def disabled(*args, **kwargs):
    return requests_cache.disabled(*args, **kwargs)


def clear():
    return requests_cache.clear()
