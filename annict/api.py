# -*- coding: utf-8 -*-
from .client import Client
from .services import (
    WorksService,
    EpisodesService,
    RecordsService,
    MeService,
)


class API(object):

    def __init__(self, client):
        self.client = client
        self.works = WorksService(client)
        self.episodes = EpisodesService(client)
        self.records = RecordsService(client)
        self.me = MeService(client)
