# -*- coding: utf-8 -*-
import requests_cache

from .client import Client
from .services import (
    WorksService,
    EpisodesService,
    RecordsService,
    MeService,
)


class API(object):

    def __init__(self, token):
        self.client = Client(token)
        self.works = WorksService(self.client)
        self.episodes = EpisodesService(self.client)
        self.records = RecordsService(self.client)
        self.me = MeService(self.client)

    @staticmethod
    def install_cache(cache_name='annict_cache', backend='memory', expire_after=180):
        requests_cache.install_cache(cache_name=cache_name, backend=backend, expire_after=expire_after)
