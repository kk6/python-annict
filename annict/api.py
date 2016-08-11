# -*- coding: utf-8 -*-
from .client import Client


class Api(object):

    def __init__(self, access_token):
        self.client = Client(access_token)

    def works(self, **kwargs):
        return self.client.get('works', **kwargs)

    def episodes(self, **kwargs):
        return self.client.get('episodes', **kwargs)

    def records(self, **kwargs):
        return self.client.get('records', **kwargs)

    def update_works_status(self, work_id, kind='no_select'):
        return self.client.post('me/statuses', work_id=work_id, kind=kind)

    def create_record(self, episode_id, **kwargs):
        return self.client.post('me/records', **kwargs)

    def update_record(self, record_id, **kwargs):
        path = '/'.join(['me/records', str(record_id)])
        return self.client.patch(path, **kwargs)

    def delete_record(self, record_id, **kwargs):
        path = '/'.join(['me/records', str(record_id)])
        return self.client.patch(path, **kwargs)

    def my_works(self, **kwargs):
        return self.client.get('me/works', **kwargs)

    def my_programs(self, **kwargs):
        return self.client.get('me/programs', **kwargs)
