# -*- coding: utf-8 -*-
import abc

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
        """Parse JSON objects into list of model instances.

        :param api: instance of :class:`API <annict.api.API>` .
        :type api: annict.api.API
        :param dict json: JSON from Annict API.
        :param str payload_type: Type of payload.
        :return: list of Model objects.
        :rtype: ResultSet

        """
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
        """Parse a JSON object into a model instance.

        :param api: instance of :class:`API <annict.api.API>` .
        :type api: annict.api.API
        :param dict json: JSON from Annict API.
        :return: :class:`User <User>` object
        :rtype: User

        """
        user = cls(api)
        user._json = json
        for k, v in json.items():
            if k == 'created_at':
                setattr(user, k, arrow.get(v).datetime)
            else:
                setattr(user, k, v)
        return user

    def following(self, fields=None, page=None, per_page=None, sort_id=None):
        """Get following information of this user.

        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: list of :class:`User <annict.models.User>` objects.
        :rtype: annict.models.ResultSet

        """
        return self._api.following(fields=fields, filter_user_id=self.id, page=page, per_page=per_page, sort_id=sort_id)

    def followers(self, fields=None, page=None, per_page=None, sort_id=None):
        """Get following information of this user.

        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: list of :class:`User <annict.models.User>` objects.
        :rtype: annict.models.ResultSet

        """
        return self._api.followers(fields=fields, filter_user_id=self.id, page=page, per_page=per_page, sort_id=sort_id)


class Work(Model):
    """Work information model"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._episodes = None

    def __repr__(self):
        return f'<Work:{self.id}:{self.title}>'

    @classmethod
    def parse(cls, api, json):
        """Parse a JSON object into a model instance.

        :param api: instance of :class:`API <annict.api.API>` .
        :type api: annict.api.API
        :param dict json: JSON from Annict API.
        :return: :class:`Work <Work>` object
        :rtype: Work

        """
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

    def episodes(self, fields=None, filter_ids=None,
                 page=None, per_page=None,
                 sort_id=None, sort_sort_number=None):
        """Get episodes information

        :reference: https://docs.annict.com/ja/api/v1/episodes.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param filter_ids: (optional) Filter results by IDs.
        :type filter_ids: list of int
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param str sort_sort_number: (optional) Sort by number for sorting. You can specify `asc` or `desc`.
        :return: list of :class:`Episode <annict.models.Episode>` objects.
        :rtype: annict.models.ResultSet

        """
        return self._api.episodes(fields=fields, filter_ids=filter_ids, filter_work_id=self.id,
                                  page=page, per_page=per_page,
                                  sort_id=sort_id, sort_sort_number=sort_sort_number)

    def select_episodes(self, *numbers):
        """Select multiple episodes

        :param numbers: Episode number.
        :return: list of :class:`Episode <Episode>`
        :rtype: list of :class:`Episode <Episode>`

        """
        if not self._episodes:
            self._episodes = self.episodes(sort_sort_number='asc')
        if not numbers:
            return self._episodes
        return [self._episodes[n - 1] for n in numbers]

    def get_episode(self, number):
        """Get Episode object

        :param number: Episode number
        :return: :class:`Episode <Episode>` object
        :rtype: Episode

        """
        return self.select_episodes(number)[0]


class Episode(Model):
    """Episode information model"""

    def __repr__(self):
        return f'<Episode:{self.id}:{self.number_text}:{self.title}:{self.work.title}>'

    @classmethod
    def parse(cls, api, json):
        """Parse a JSON object into a model instance.

        :param api: instance of :class:`API <annict.api.API>` .
        :type api: annict.api.API
        :param dict json: JSON from Annict API.
        :return: :class:`Episode <Episode>` object
        :rtype: Episode

        """
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
        :param bool share_twitter: (optional) Whether to share the record on Twitter.
            You can enter `True` or `False`.
        :param bool share_facebook: (optional) Whether to share the record on Facebook.
            You can enter `True` or `False`.
        :return: :class:`Record <annict.models.Record>` object.
        """
        return self._api.create_record(self.id, comment, rating, share_twitter, share_facebook)


class Record(Model):
    """Record information model"""

    def __repr__(self):
        return f'<Record:{self.id}>'

    @classmethod
    def parse(cls, api, json):
        """Parse a JSON object into a model instance.

        :param api: instance of :class:`API <annict.api.API>` .
        :type api: annict.api.API
        :param dict json: JSON from Annict API.
        :return: :class:`Record <Record>` object
        :rtype: Record

        """
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
        :param bool share_twitter: (optional) Whether to share the record on Twitter.
            You can enter `True` or `False`.
        :param bool share_facebook: (optional) Whether to share the record on Facebook.
            You can enter `True` or `False`.
        :return: :class:`Record <annict.models.Record>` object after edit.

        """
        return self._api.edit_record(self.id, comment, rating, share_twitter, share_facebook)

    def delete(self):
        """Delete the created record.

        :return: Returns `True` if deletion succeeded.

        """
        return self._api.delete_record(self.id)


class Program(Model):
    """Program information model"""

    def __repr__(self):
        return f'<Program:{self.id}>'

    @classmethod
    def parse(cls, api, json):
        """Parse a JSON object into a model instance.

        :param api: instance of :class:`API <annict.api.API>` .
        :type api: annict.api.API
        :param dict json: JSON from Annict API.
        :return: :class:`Program <Program>` object
        :rtype: Program

        """
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
        """Parse a JSON object into a model instance.

        :param api: instance of :class:`API <annict.api.API>` .
        :type api: annict.api.API
        :param dict json: JSON from Annict API.
        :return: :class:`Activity <Activity>` object
        :rtype: Activity

        """
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
