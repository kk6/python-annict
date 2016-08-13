# -*- coding: utf-8 -*-
from operator import methodcaller

import arrow


def cached_children(name):
    def cached(f):
        def _cached(self, *args, **kwargs):
            if not self._children:
                m = methodcaller('request_{}_list'.format(name))
                m(self)
            return f(self, *args, **kwargs)
        return _cached
    return cached


class ResultSet(list):
    def __init__(self, total_count, prev_page=None, next_page=None):
        super().__init__()
        self.total_count = total_count
        self.prev_page = prev_page
        self.next_page = next_page


class Model(object):

    def __init__(self, api=None):
        self._api = api
        self._children = []

    @classmethod
    def parse(cls, api, json):
        """Parse a JSON object into a model instance."""
        raise NotImplementedError

    @classmethod
    def parse_list(cls, api, json, payload_type):
        results = ResultSet(
            total_count=json['total_count'],
            prev_page=json['prev_page'],
            next_page=json['next_page'],
        )
        results._json = json
        for obj in json['{}s'.format(payload_type)]:
            if obj:
                results.append(cls.parse(api, obj))
        return results


class User(Model):

    @classmethod
    def parse(cls, api, json):
        user = cls(api)
        user._json = json
        for k, v in json.items():
            if k == 'created_at':
                setattr(user, k, arrow.get(v).datetime)
            else:
                setattr(user, k, v)
        return user


class Work(Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def parse(cls, api, json):
        work = cls(api)
        work._json = json
        for k, v in json.items():
            if k == 'released_on':
                if v:
                    date = arrow.get(v).date()
                else:
                    date = None
                setattr(work, k, date)
            else:
                setattr(work, k, v)
        return work

    def request_episode_list(self):
        self._children = self._api.episodes.get(filter_work_id=self.id, sort_sort_number='asc')

    @cached_children('episode')
    def get_episode(self, number):
        return self._children[number - 1]

    @cached_children('episode')
    def select_episodes(self, *numbers):
        if not numbers:
            return self._children
        return [self._children[n - 1] for n in numbers]


class Episode(Model):

    @classmethod
    def parse(cls, api, json):
        episode = cls(api)
        episode._json = json
        for k, v in json.items():
            if k == 'episode':
                setattr(episode, 'episode_id', v)
            elif k == 'work':
                work = Work.parse(api, v)
                setattr(episode, k, work)
            elif k == 'prev_episode' and v:
                prev_episode = cls.parse(api, v)
                setattr(episode, k, prev_episode)
            elif k == 'next_episode' and v:
                next_episode = cls.parse(api, v)
                setattr(episode, k, next_episode)
            else:
                setattr(episode, k, v)
        return episode

    def create_record(self, **kwargs):
        return self._api.me.records.create(self.id, **kwargs)


class Record(Model):

    @classmethod
    def parse(cls, api, json):
        record = cls(api)
        record._json = json
        for k, v in json.items():
            if k == 'created_at':
                setattr(record, k, arrow.get(v).datetime)
            elif k == 'user':
                user = User.parse(api, v)
                setattr(record, k, user)
            elif k == 'work':
                work = Work.parse(api, v)
                setattr(record, k, work)
            elif k == 'episode':
                episode = Episode.parse(api, v)
                setattr(record, k, episode)
            else:
                setattr(record, k, v)
        return record

    def update(self, **kwargs):
        return self._api.me.records.update(self.id, **kwargs)

    def delete(self):
        return self._api.me.records.delete(self.id)


class Program(Model):

    @classmethod
    def parse(cls, api, json):
        program = cls(api)
        program._json = json
        for k, v in json.items():
            if k == 'started_at':
                setattr(program, k, arrow.get(v).datetime)
            elif k == 'work':
                work = Work.parse(api, v)
                setattr(program, k, work)
            elif k == 'episode':
                episode = Episode.parse(api, v)
                setattr(program, k, episode)
            else:
                setattr(program, k, v)
        return program


MODEL_MAPPING = {
    'user': User,
    'work': Work,
    'episode': Episode,
    'record': Record,
    'program': Program,
}
