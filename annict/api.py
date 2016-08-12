# -*- coding: utf-8 -*-
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
