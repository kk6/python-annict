# -*- coding: utf-8 -*-
from .utils import stringify


class ServiceBase(object):
    path = ''
    allowed_params = []

    def __init__(self, client):
        self.client = client

    def _build_parameters(self, kwargs):
        params = {}
        for k, v in kwargs.items():
            if k in self.allowed_params:
                params[k] = stringify(v)
        return params


class WorksService(ServiceBase):
    """
    :reference: https://annict.wikihub.io/wiki/api/works
    """
    path = 'works'
    allowed_params = ['fields', 'filter_ids', 'filter_season', 'filter_title',
                      'page', 'per_page',
                      'sort_id' 'sort_season', 'sort_watchers_count']

    def get(self, **kwargs):
        params = self._build_parameters(kwargs)
        return self.client.get(self.path, params)


class EpisodesService(ServiceBase):
    """
    :reference: https://annict.wikihub.io/wiki/api/episodes
    """
    path = 'episodes'
    allowed_params = ['fields', 'filter_ids', 'filter_work_ids', 'page', 'per_page',
                      'sort_id', 'sort_sort_number']

    def get(self, **kwargs):
        params = self._build_parameters(kwargs)
        return self.client.get(self.path, params)


class RecordsService(ServiceBase):
    """
    :reference: https://annict.wikihub.io/wiki/api/records
    """
    path = 'records'
    allowed_params = ['fields', 'filter_ids', 'filter_episode_id', 'page', 'per_page',
                      'sort_id', 'sort_like_count']

    def get(self, **kwargs):
        params = self._build_parameters(kwargs)
        return self.client.get(self.path, params)


class MeStatusesService(ServiceBase):
    """
    :reference: https://annict.wikihub.io/wiki/api/me-statuses
    """
    path = 'me/statuses'

    def create(self, work_id, kind):
        return self.client.post(self.path, {'work_id': work_id, 'kind': kind})


class MeRecordsService(ServiceBase):
    """
    :reference: https://annict.wikihub.io/wiki/api/me-records
    """
    path = 'me/records'
    allowed_params = ['comment', 'rating', 'share_twitter', 'share_facebook']

    def create(self, episode_id, **kwargs):
        params = self._build_parameters(kwargs)
        params['episode_id'] = episode_id
        return self.client.post(self.path, params)

    def update(self, record_id, **kwargs):
        params = self._build_parameters(kwargs)
        path = '/'.join([self.path, record_id])
        return self.client.patch(path, params)

    def delete(self, record_id):
        path = '/'.join([self.path, record_id])
        return self.client.delete(path)


class MeWorksService(ServiceBase):
    """
    :reference: https://annict.wikihub.io/wiki/api/me-works
    """
    path = 'me/works'
    allowed_params = ['fields', 'filter_ids', 'filter_season', 'filter_title', 'filter_status',
                      'page', 'per_page', 'sort_id', 'sort_season', 'sort_watchers_count']

    def get(self, **kwargs):
        params = self._build_parameters(kwargs)
        return self.client.get(self.path, params)


class MeProgramsService(ServiceBase):
    """
    :reference: https://annict.wikihub.io/wiki/api/me-programs
    """
    path = 'me/programs'
    allowed_params = ['fields', 'filter_ids', 'filter_channel_ids', 'filter_work_ids',
                      'filter_started_at_gt', 'filter_started_at_lt', 'filter_unwatched',
                      'filter_rebroadcast', 'page', 'per_page', 'sort_id', 'sort_started_at']

    def get(self, **kwargs):
        params = self._build_parameters(kwargs)
        return self.client.get(self.path, params)


class MeService(object):

    def __init__(self, client):
        self.statuses = MeStatusesService(client)
        self.records = MeRecordsService(client)
        self.works = MeWorksService(client)
        self.programs = MeProgramsService(client)
