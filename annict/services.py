# -*- coding: utf-8 -*-
from .utils import stringify


class ServiceBase(object):
    path = ''
    allowed_params = []
    payload_type = ''

    def __init__(self, client, parser):
        self.client = client
        self.parser = parser

    def build_parameters(self, kwargs):
        params = {}
        for k, v in kwargs.items():
            if k in self.allowed_params:
                params[k] = stringify(v)
        return params


class WorksService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/works.html
    """
    path = 'works'
    allowed_params = ['fields', 'filter_ids', 'filter_season', 'filter_title',
                      'page', 'per_page',
                      'sort_id' 'sort_season', 'sort_watchers_count']
    payload_type = 'work'

    def get(self, **kwargs):
        params = self.build_parameters(kwargs)
        json = self.client.get(self.path, params)
        return self.parser.parse(json, self.payload_type)


class EpisodesService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/episodes.html
    """
    path = 'episodes'
    allowed_params = ['fields', 'filter_ids', 'filter_work_id', 'page', 'per_page',
                      'sort_id', 'sort_sort_number']
    payload_type = 'episode'

    def get(self, **kwargs):
        params = self.build_parameters(kwargs)
        json = self.client.get(self.path, params)
        return self.parser.parse(json, self.payload_type)


class RecordsService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/records.html
    """
    path = 'records'
    allowed_params = ['fields', 'filter_ids', 'filter_episode_id', 'filter_has_record_comment',
                      'page', 'per_page', 'sort_id', 'sort_like_count']
    payload_type = 'record'

    def get(self, **kwargs):
        params = self.build_parameters(kwargs)
        json = self.client.get(self.path, params)
        return self.parser.parse(json, self.payload_type)


class UsersService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/users.html
    """
    path = 'users'
    allowed_params = ['fields', 'filter_ids', 'filter_usernames', 'page', 'per_page',
                      'sort_id']
    payload_type = 'user'

    def get(self, **kwargs):
        params = self.build_parameters(kwargs)
        json = self.client.get(self.path, params)
        return self.parser.parse(json, self.payload_type)


class FollowingService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/following.html
    """
    path = 'following'
    allowed_params = ['fields', 'filter_user_id', 'filter_username', 'page', 'per_page',
                      'sort_id']
    payload_type = 'user'

    def get(self, **kwargs):
        params = self.build_parameters(kwargs)
        json = self.client.get(self.path, params)
        return self.parser.parse(json, self.payload_type)


class FollowersService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/followers.html
    """
    path = 'followers'
    allowed_params = ['fields', 'filter_user_id', 'filter_username', 'page', 'per_page',
                      'sort_id']
    payload_type = 'user'

    def get(self, **kwargs):
        params = self.build_parameters(kwargs)
        json = self.client.get(self.path, params)
        return self.parser.parse(json, self.payload_type)


class MeService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/me.html
    """
    path = 'me'
    allowed_params = ['fields']
    payload_type = 'user'

    def __init__(self, client, parser):
        super().__init__(client, parser)
        self.statuses = MeStatusesService(client, parser)
        self.records = MeRecordsService(client, parser)
        self.works = MeWorksService(client, parser)
        self.programs = MeProgramsService(client, parser)

    def get(self, **kwargs):
        params = self.build_parameters(kwargs)
        json = self.client.get(self.path, params)
        return self.parser.parse(json, self.payload_type)


class MeStatusesService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/me-statuses.html
    """
    path = 'me/statuses'

    def create(self, work_id, kind):
        return self.client.post(self.path, {'work_id': work_id, 'kind': kind})


class MeRecordsService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/me-records.html
    """
    path = 'me/records'
    allowed_params = ['comment', 'rating', 'share_twitter', 'share_facebook']
    payload_type = 'record'

    def create(self, episode_id, **kwargs):
        params = self.build_parameters(kwargs)
        params['episode_id'] = episode_id
        json = self.client.post(self.path, params)
        return self.parser.parse(json, self.payload_type)

    def update(self, record_id, **kwargs):
        params = self.build_parameters(kwargs)
        path = '/'.join([self.path, str(record_id)])
        json = self.client.patch(path, params)
        return self.parser.parse(json, self.payload_type)

    def delete(self, record_id, **kwargs):
        path = '/'.join([self.path, str(record_id)])
        return self.client.delete(path, kwargs)


class MeWorksService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/me-works.html
    """
    path = 'me/works'
    allowed_params = ['fields', 'filter_ids', 'filter_season', 'filter_title', 'filter_status',
                      'page', 'per_page', 'sort_id', 'sort_season', 'sort_watchers_count']
    payload_type = 'work'

    def get(self, **kwargs):
        params = self.build_parameters(kwargs)
        json = self.client.get(self.path, params)
        return self.parser.parse(json, self.payload_type)


class MeProgramsService(ServiceBase):
    """
    :reference: https://docs.annict.com/ja/api/v1/me-programs.html
    """
    path = 'me/programs'
    allowed_params = ['fields', 'filter_ids', 'filter_channel_ids', 'filter_work_ids',
                      'filter_started_at_gt', 'filter_started_at_lt', 'filter_unwatched',
                      'filter_rebroadcast', 'page', 'per_page', 'sort_id', 'sort_started_at']
    payload_type = 'program'

    def get(self, **kwargs):
        params = self.build_parameters(kwargs)
        json = self.client.get(self.path, params)
        return self.parser.parse(json, self.payload_type)
