# -*- coding: utf-8 -*-
from .services import APIMethod
from .parsers import ModelParser
from .cursors import cursor_support


class API(object):
    """API wrapper for Annict.

    Basic Usage::

        >>> from annict.api import API
        >>> api = API('your-access-token')
        >>> api.me()
        <User:1229:あしやひろ:@kk6>

    """
    def __init__(self, token, base_url='https://api.annict.com', api_version='v1', parser=ModelParser):
        self.token = token
        self.base_url = base_url
        self.api_version = api_version
        self.parser = parser(self)

    @cursor_support
    def works(self, fields=None, filter_ids=None, filter_season=None, filter_title=None,
              page=None, per_page=None,
              sort_id=None, sort_season=None, sort_watchers_count=None):
        """Get works information

        :reference: https://docs.annict.com/ja/api/v1/works.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param filter_ids: (optional) Filter results by IDs.
        :type filter_ids: list of int
        :param str filter_season: (optional) Filter results by release time of season.
        :param str filter_title: (optional) Filter results by title.
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param str sort_season: (optional) Sort the results by their release time of season.
            You can specify `asc` or `desc`.
        :param str sort_watchers_count: (optional) Sort the results by their watchers count.
            You can specify `asc` or `desc`.
        :return: list of :class:`Work <annict.models.Work>` objects.
        :rtype: annict.models.ResultSet

        """
        api_method = APIMethod(
            api=self,
            path='works',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_season', 'filter_title',
                            'page', 'per_page',
                            'sort_id', 'sort_season', 'sort_watchers_count'),
            payload_type='work',
            payload_is_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    @cursor_support
    def episodes(self, fields=None, filter_ids=None, filter_work_id=None,
                 page=None, per_page=None,
                 sort_id=None, sort_sort_number=None):
        """Get episodes information

        :reference: https://docs.annict.com/ja/api/v1/episodes.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param filter_ids: (optional) Filter results by IDs.
        :type filter_ids: list of int
        :param int filter_work_id: (optional) Filter results by Work's ID.
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param str sort_sort_number: (optional) Sort by number for sorting. You can specify `asc` or `desc`.
        :return: list of :class:`Episode <annict.models.Episode>` objects.
        :rtype: annict.models.ResultSet

        """
        api_method = APIMethod(
            api=self,
            path='episodes',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_work_id',
                            'page', 'per_page', 'sort_id', 'sort_sort_number'),
            payload_type='episode',
            payload_is_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    @cursor_support
    def records(self, fields=None, filter_ids=None, filter_episode_id=None, filter_has_record_comment=None,
                page=None, per_page=None,
                sort_id=None, sort_likes_count=None):
        """Get records to episodes

        :reference: https://docs.annict.com/ja/api/v1/records.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param filter_ids: (optional) Filter results by IDs.
        :type filter_ids: list of int
        :param int filter_episode_id: (optional) Filter results by Episode's ID.
        :param bool filter_has_record_comment: (optional) Filter the results by the presence or absence of comments.
            If you specify `True`, only records with comments will be filtered.
            Specifying `False` Filter records without comments.
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param str sort_likes_count: (optional) Sort the results by their number of likes.
            You can specify `asc` or `desc`.
        :return: list of :class:`Record <annict.models.Record>` objects.
        :rtype: annict.models.ResultSet

        """
        api_method = APIMethod(
            api=self,
            path='records',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_episode_id', 'filter_has_record_comment',
                            'page', 'per_page', 'sort_id', 'sort_likes_count'),
            payload_type='record',
            payload_is_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    @cursor_support
    def search_users(self, fields=None, filter_ids=None, filter_usernames=None,
                     page=None, per_page=None,
                     sort_id=None):
        """Get users information

        :reference: https://docs.annict.com/ja/api/v1/users.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param filter_ids: (optional) Filter results by IDs.
        :type filter_ids: list of int
        :param filter_usernames: (optional) Filter results by usernames.
        :type filter_usernames: list of str
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: list of :class:`User <annict.models.User>` objects.
        :rtype: annict.models.ResultSet

        """
        api_method = APIMethod(
            api=self,
            path='users',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_usernames', 'page', 'per_page', 'sort_id'),
            payload_type='user',
            payload_is_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    @cursor_support
    def following(self, fields=None, filter_user_id=None, filter_username=None,
                  page=None, per_page=None,
                  sort_id=None):
        """Get following information

        :reference: https://docs.annict.com/ja/api/v1/following.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param int filter_user_id: (optional) Filter results by User's ID.
        :param str filter_username: (optional) Filter results by username.
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: list of :class:`User <annict.models.User>` objects.
        :rtype: annict.models.ResultSet

        """
        api_method = APIMethod(
            api=self,
            path='following',
            method='GET',
            allowed_params=('fields', 'filter_user_id', 'filter_username', 'page', 'per_page', 'sort_id'),
            payload_type='user',
            payload_is_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    @cursor_support
    def followers(self, fields=None, filter_user_id=None, filter_username=None,
                  page=None, per_page=None,
                  sort_id=None):
        """Get followers information

        :reference: https://docs.annict.com/ja/api/v1/followers.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param int filter_user_id: (optional) Filter results by User's ID.
        :param str filter_username: (optional) Filter results by username.
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: list of :class:`User <annict.models.User>` objects.
        :rtype: annict.models.ResultSet

        """
        api_method = APIMethod(
            api=self,
            path='followers',
            method='GET',
            allowed_params=('fields', 'filter_user_id', 'filter_username', 'page', 'per_page', 'sort_id'),
            payload_type='user',
            payload_is_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    @cursor_support
    def activities(self, fields=None, filter_user_id=None, filter_username=None,
                   page=None, per_page=None,
                   sort_id=None):
        """Get activities

        :reference: https://docs.annict.com/ja/api/v1/activities.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param int filter_user_id: (optional) Filter results by User's ID.
        :param str filter_username: (optional) Filter results by username.
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: list of :class:`Activity <annict.models.Activity>` objects.
        :rtype: annict.models.ResultSet

        """
        api_method = APIMethod(
            api=self,
            path='activities',
            method='GET',
            allowed_params=('fields', 'filter_user_id', 'filter_username', 'page', 'per_page', 'sort_id'),
            payload_type='activity',
            payload_is_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def me(self, fields=None):
        """Get your profile information

        :reference: https://docs.annict.com/ja/api/v1/me.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :return: :class:`User <annict.models.User>` object of your user information.

        """
        api_method = APIMethod(
            api=self,
            path='me',
            method='GET',
            allowed_params=('fields',),
            payload_type='user',
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def set_status(self, work_id, kind):
        """Set the status of the work.

        :reference: https://docs.annict.com/ja/api/v1/me-statuses.html
        :param int work_id: Work's ID
        :param str kind: Types of status.
            You can specify `wanna_watch`, `watching`, `watched`, `on_hold`, `stop_watching`, or `no_select`.
        :return: Returns `True` if deletion succeeded.

        """
        api_method = APIMethod(
            api=self,
            path='me/statuses',
            method='POST',
            allowed_params=('work_id', 'kind'),
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def create_record(self, episode_id, comment=None, rating=None, share_twitter=False, share_facebook=False):
        """Create a record to the episode.

        :reference: https://docs.annict.com/ja/api/v1/me-records.html
        :param int episode_id: Episode's ID
        :param str comment: (optional) Comment.
        :param float rating: (optional) Rating.
        :param bool share_twitter: (optional) Whether to share the record on Twitter. You can enter `True` or `False`.
        :param bool share_facebook: (optional) Whether to share the record on Facebook. You can enter `True` or `False`.
        :return: :class:`Record <annict.models.Record>` object.

        """
        api_method = APIMethod(
            api=self,
            path='me/records',
            method='POST',
            allowed_params=('episode_id', 'comment', 'rating', 'share_twitter', 'share_facebook'),
            payload_type='record',
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def edit_record(self, id_, comment=None, rating=None, share_twitter=False, share_facebook=False):
        """Edit the created record.

        :reference: https://docs.annict.com/ja/api/v1/me-records.html
        :param int id_: Record's ID.
        :param str comment: (optional) Comment.
        :param float rating: (optional) Rating.
        :param bool share_twitter: (optional) Whether to share the record on Twitter. You can enter `True` or `False`.
        :param bool share_facebook: (optional) Whether to share the record on Facebook. You can enter `True` or `False`.
        :return: :class:`Record <annict.models.Record>` object after update.

        """
        api_method = APIMethod(
            api=self,
            path='me/records',
            method='PATCH',
            allowed_params=('comment', 'rating', 'share_twitter', 'share_facebook'),
            payload_type='record',
        )
        api_method.build_path(id_)
        params = api_method.build_parameters(locals())
        return api_method(params)

    def delete_record(self, id_):
        """Delete the created record.

        :reference: https://docs.annict.com/ja/api/v1/me-records.html
        :param int id_: Recode's ID
        :return: Returns `True` if deletion succeeded.

        """
        api_method = APIMethod(
            api=self,
            path='me/records',
            method='DELETE',
            allowed_params=(),
        )
        api_method.build_path(id_)
        params = api_method.build_parameters(locals())
        return api_method(params)

    @cursor_support
    def my_works(self, fields=None, filter_ids=None, filter_season=None, filter_title=None, filter_status=None,
                 page=None, per_page=None,
                 sort_id=None, sort_season=None, sort_watchers_count=None):
        """Get the information of the work you are setting status.

        :reference: https://docs.annict.com/ja/api/v1/me-works.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param filter_ids: (optional) Filter results by IDs.
        :type filter_ids: list of int
        :param str filter_season: (optional) Filter results by release time of season.
        :param str filter_title: (optional) Filter results by title.
        :param str filter_status: (optional) Filter results by status.
            You can specify `wanna_watch`, `watching`, `watched`, `on_hold`, `stop_watching`.
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param str sort_season: (optional) Sort the results by their release time of season.
            You can specify `asc` or `desc`.
        :param str sort_watchers_count: (optional) Sort the results by their watchers count.
            You can specify `asc` or `desc`.
        :return: list of :class:`Work <annict.models.Work>` objects.
        :rtype: annict.models.ResultSet

        """
        api_method = APIMethod(
            api=self,
            path='me/works',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_season', 'filter_title', 'filter_status',
                            'page', 'per_page', 'sort_id', 'sort_season', 'sort_watchers_count'),
            payload_type='work',
            payload_is_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    @cursor_support
    def my_programs(self, fields=None, filter_ids=None, filter_channel_ids=None, filter_work_ids=None,
                    filter_started_at_gt=None, filter_started_at_lt=None,
                    filter_unwatched=None, filter_rebroadcast=None,
                    page=None, per_page=None,
                    sort_id=None, sort_started_at=None):
        """Get the broadcast schedule.

        :reference: https://docs.annict.com/ja/api/v1/me-programs.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param filter_ids: (optional) Filter results by IDs.
        :type filter_ids: list of int
        :param filter_channel_ids: (optional) Filter results by Channel IDs.
        :type filter_channel_ids: list of int
        :param filter_work_ids: (optional) Filter results by Work IDs.
        :type filter_work_ids: list of int
        :param datetime filter_started_at_gt: (optional) Filter results results to those with the broadcast start date
            and time after the specified date and time.
        :param datetime filter_started_at_lt: (optional) Filter results results to those with the broadcast start date
            and time before the specified date and time.
        :param bool filter_unwatched: (optional) Only get unwatched broadcast schedules.
        :param bool filter_rebroadcast: (optional) Filter the broadcast schedule based on the rebroadcast flag.
            If you pass `True`, only rebroadcasting,
            passing `False` will get broadcast schedules other than rebroadcast.
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param str sort_started_at: (optional) Sort the results by started_at.
        :return: list of :class:`Program <annict.models.Program>` objects.
        :rtype: annict.models.ResultSet

        """
        api_method = APIMethod(
            api=self,
            path='me/programs',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_channel_ids', 'filter_work_ids', 'filter_started_at_gt',
                            'filter_started_at_lt', 'filter_unwatched', 'filter_rebroadcast',
                            'page', 'per_page', 'sort_id', 'sort_started_at'),
            payload_type='program',
            payload_is_list=True
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    @cursor_support
    def following_activities(self, fields=None, filter_actions=None, filter_muted=None,
                             page=None, per_page=None,
                             sort_id=None):
        """Get the activity of the user you are following.

        :reference: https://docs.annict.com/ja/api/v1/me-following-activities.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :type fields: list of str
        :param str filter_actions: (optional) Filter results by action
            (create_record|create_multiple_records|create_status).
        :param bool filter_muted: (optional) Specify whether to exclude muted users with the mute function.
            You can exclude with `True` and not exclude with `False`. The default is `True` (exclude).
        :param int page: (optional) Specify the number of pages.
        :param int per_page: (optional) Specify how many items to acquire per page.
        :param str sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: list of :class:`Activity <annict.models.Activity>` objects.
        :rtype: annict.models.ResultSet

        """
        api_method = APIMethod(
            api=self,
            path='me/following_activities',
            method='GET',
            allowed_params=('fields', 'filter_actions', 'filter_muted', 'page', 'per_page', 'sort_id'),
            payload_type='activity',
            payload_is_list=True
        )
        params = api_method.build_parameters(locals())
        return api_method(params)
