# -*- coding: utf-8 -*-
from .client import Client
from .services import (
    WorksService,
    EpisodesService,
    RecordsService,
    MeService,
)
from .parsers import ModelPerser


class API(object):

    def __init__(self, token, parser=ModelPerser):
        self.client = Client(token)
        self.works = WorksService(self.client, parser(self))
        self.episodes = EpisodesService(self.client, parser(self))
        self.records = RecordsService(self.client, parser(self))
        self.me = MeService(self.client, parser(self))
