# -*- coding: utf-8 -*-


class ServiceBase(object):
    path = ''
    allowed_options = []

    def __init__(self, client):
        self.client = client

    def _build_options(self, kwargs):
        options = {}
        for k, v in kwargs.items():
            if k in self.allowed_options:
                options[k] = v
        return options


class WorksService(ServiceBase):
    path = 'works'
    allowed_params = ['fields', 'filter_ids', 'filter_season', 'filter_title',
                      'page', 'per_page',
                      'sort_id' 'sort_season', 'sort_watchers_count']

    def get(self, **kwargs):
        options = self._build_options(kwargs)
        return self.client.get(self.path, options)


class EpisodesService(ServiceBase):
    path = 'episodes'
    allowed_options = ['fields', 'filter_ids', 'filter_work_ids', 'page', 'per_page',
                       'sort_id', 'sort_sort_number']

    def get(self, **kwargs):
        options = self._build_options(kwargs)
        return self.client.get(self.path, options)


class RecordsService(ServiceBase):
    path = 'records'
    allowed_options = ['fields', 'filter_ids', 'filter_episode_id', 'page', 'per_page',
                       'sort_id', 'sort_like_count']

    def get(self, **kwargs):
        options = self._build_options(kwargs)
        return self.client.get(self.path, options)


class MeStatusesService(ServiceBase):
    path = 'me/statuses'

    def post(self, work_id, kind):
        return self.client.post(self.path, {'work_id': work_id, 'kind': kind})


class MeRecordsService(ServiceBase):
    path = 'me/records'
    allowed_options = ['comment', 'rating', 'share_twitter', 'share_facebook']

    def create(self, episode_id, **kwargs):
        options = self._build_options(kwargs)
        options['episode_id'] = episode_id
        return self.client.post(self.path, options)

    def update(self, record_id, **kwargs):
        options = self._build_options(kwargs)
        path = '/'.join([self.path, record_id])
        return self.client.patch(path, options)

    def delete(self, record_id):
        path = '/'.join([self.path, record_id])
        return self.client.delete(path)


class MeWorksService(ServiceBase):
    path = 'me/works'
    allowed_options = ['fields', 'filter_ids', 'filter_season', 'filter_title', 'filter_status',
                       'page', 'per_page', 'sort_id', 'sort_season', 'sort_watchers_count']

    def get(self, **kwargs):
        options = self._build_options(kwargs)
        return self.client.get(self.path, options)


class MeProgramsService(ServiceBase):
    path = 'me/programs'
    allowed_options = ['fields', 'filter_ids', 'filter_channel_ids', 'filter_work_ids',
                       'filter_started_at_gt', 'filter_started_at_lt', 'filter_unwatched',
                       'filter_rebroadcast', 'page', 'per_page', 'sort_id', 'sort_started_at']

    def get(self, **kwargs):
        options = self._build_options(kwargs)
        return self.client.get(self.path, options)


class MeService(object):

    def __init__(self, client):
        self.statuses = MeStatusesService(client)
        self.records = MeRecordsService(client)
        self.works = MeWorksService(client)
        self.programs = MeProgramsService(client)
