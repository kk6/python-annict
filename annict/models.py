# -*- coding: utf-8 -*-
import abc
from operator import methodcaller

import arrow


class ResultSet(list):
    """A list like object that holds results from an Annict API query."""

    def __init__(self, total_count, prev_page=None, next_page=None):
        super().__init__()
        self.total_count = total_count
        self.prev_page = prev_page
        self.next_page = next_page


class Model(metaclass=abc.ABCMeta):
    """Abstract class of each models."""

    def __init__(self, api=None):
        self._api = api
        self._children = []

    @classmethod
    @abc.abstractmethod
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
        if payload_type == 'activity':
            pluralized_payload_name = 'activities'
        else:
            pluralized_payload_name = '{}s'.format(payload_type)
        for obj in json[pluralized_payload_name]:
            if obj:
                results.append(cls.parse(api, obj))
        return results


class User(Model):
    """User information model"""

    def __repr__(self):
        return f'<User:{self.id}:{self.name}:@{self.username}>'

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
    """Work information model"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Work:{self.id}:{self.title}>'

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

    def set_status(self, kind):
        """Set the status of the work.
        
        :param str kind: Types of status.
            You can specify `wanna_watch`, `watching`, `watched`, `on_hold`, `stop_watching`, or `no_select`.
        :return: Returns `True` if deletion succeeded.

        """
        return self._api.set_status(self.id, kind)

    def request_episode_list(self):
        self._children = self._api.episodes(filter_work_id=self.id, sort_sort_number='asc')

    def get_episode(self, number):
        """Get Episode object
        
        :param number: Episode number
        :return: :class:`Episode <Episode>` object
        :rtype: Episode

        """
        return self._children[number - 1]

    def select_episodes(self, *numbers):
        if not numbers:
            return self._children
        return [self._children[n - 1] for n in numbers]


class Episode(Model):
    """Episode information model"""

    def __repr__(self):
        return f'<Episode:{self.id}:{self.number_text}:{self.title}:{self.work.title}>'

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

    def create_record(self, comment=None, rating=None, share_twitter=False, share_facebook=False):
        """Create a record for this episode.
        
        :param str comment: (optional) Comment.
        :param float rating: (optional) Rating.
        :param bool share_twitter: (optional) Whether to share the record on Twitter. You can enter `True` or `False`. 
        :param bool share_facebook: (optional) Whether to share the record on Facebook. You can enter `True` or `False`.
        :return: :class:`Record <annict.models.Record>` object.
        """
        return self._api.create_record(self.id, comment, rating, share_twitter, share_facebook)


class Record(Model):
    """Record information model"""

    def __repr__(self):
        return f'<Record:{self.id}>'

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

    def edit(self, comment=None, rating=None, share_twitter=False, share_facebook=False):
        """Edit the created record.
        
        :param str comment: (optional) Comment.
        :param float rating: (optional) Rating.
        :param bool share_twitter: (optional) Whether to share the record on Twitter. You can enter `True` or `False`. 
        :param bool share_facebook: (optional) Whether to share the record on Facebook. You can enter `True` or `False`.
        :return: :class:`Record <annict.models.Record>` object after edit.

        """
        return self._api.edit_record(self.id, comment, rating, share_twitter, share_facebook)

    def delete(self):
        return self._api.delete_record(self.id)


class Program(Model):
    """Program information model"""

    def __repr__(self):
        return f'<Program:{self.id}>'

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


class Activity(Model):
    """Activity information model"""

    def __repr__(self):
        return f'<Activity:{self.action}:@{self.user.username}>'

    @classmethod
    def parse(cls, api, json):
        activity = cls(api)
        activity._json = json
        for k, v in json.items():
            if k == 'created_at':
                setattr(activity, k, arrow.get(v).datetime)
            elif k == 'user':
                user = User.parse(api, v)
                setattr(activity, k, user)
            elif k == 'work':
                work = Work.parse(api, v)
                setattr(activity, k, work)
            elif k == 'episode':
                episode = Episode.parse(api, v)
                setattr(activity, k, episode)
            else:
                setattr(activity, k, v)
        return activity


MODEL_MAPPING = {
    'user': User,
    'work': Work,
    'episode': Episode,
    'record': Record,
    'program': Program,
    'activity': Activity,
}
