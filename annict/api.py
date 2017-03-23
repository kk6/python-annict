# -*- coding: utf-8 -*-
from .client import Client
from .services import (
    WorksService,
    EpisodesService,
    RecordsService,
    UsersService,
    FollowingService,
    FollowersService,
    ActivitiesService,
    MeService,
)
from .parsers import ModelParser


class API(object):

    def __init__(self, token, parser=ModelParser):
        self.client = Client(token)
        self.works = WorksService(self.client, parser(self))
        self.episodes = EpisodesService(self.client, parser(self))
        self.records = RecordsService(self.client, parser(self))
        self.users = UsersService(self.client, parser(self))
        self.following = FollowingService(self.client, parser(self))
        self.followers = FollowersService(self.client, parser(self))
        self.activities = ActivitiesService(self.client, parser(self))
        self.me = MeService(self.client, parser(self))
