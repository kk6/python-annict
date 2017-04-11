# -*- coding: utf-8 -*-
from .services import APIMethod
from .parsers import ModelParser


class API(object):
    """API wrapper for Annict."""

    def __init__(self, token, base_url='https://api.annict.com', api_version='v1', parser=ModelParser):
        self.token = token
        self.base_url = base_url
        self.api_version = api_version
        self.parser = parser(self)

    def works(self, fields=None, filter_ids=None, filter_season=None, filter_title=None,
              page=None, per_page=None,
              sort_id=None, sort_season=None, sort_watchers_count=None):
        """Get works information

        :reference: https://docs.annict.com/ja/api/v1/works.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :param filter_ids: (optional) Filter results by IDs.
        :param filter_season: (optional) Filter results by release time of season.
        :param filter_title: (optional) Filter results by title.
        :param page: (optional) Specify the number of pages.
        :param per_page: (optional) Specify how many items to acquire per page.
        :param sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param sort_season: (optional) Sort the results by their release time of season. You can specify `asc` or `desc`.
        :param sort_watchers_count: (optional) Sort the results by their watchers count. You can specify `asc` or `desc`.
        :return: List of `Work` objects.

        """
        api_method = APIMethod(
            api=self,
            path='works',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_season', 'filter_title',
                            'page', 'per_page',
                            'sort_id', 'sort_season', 'sort_watchers_count'),
            payload_type='work',
            payload_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def episodes(self, fields=None, filter_ids=None, filter_work_id=None,
                 page=None, per_page=None,
                 sort_id=None, sort_sort_number=None):
        """Get episodes information

        :reference: https://docs.annict.com/ja/api/v1/episodes.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :param filter_ids: (optional) Filter results by IDs.
        :param filter_work_id: (optional) Filter results by Work's ID.
        :param page: (optional) Specify the number of pages.
        :param per_page: (optional) Specify how many items to acquire per page.
        :param sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param sort_sort_number: (optional) Sort by number for sorting. You can specify `asc` or `desc`.
        :return: List of `Episode` objects.

        """
        api_method = APIMethod(
            api=self,
            path='episodes',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_work_id',
                            'page', 'per_page', 'sort_id', 'sort_sort_number'),
            payload_type='episode',
            payload_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def records(self, fields=None, filter_ids=None, filter_episode_id=None, filter_has_record_comment=None,
                page=None, per_page=None,
                sort_id=None, sort_likes_count=None):
        """Get records to episodes

        :reference: https://docs.annict.com/ja/api/v1/records.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :param filter_ids: (optional) Filter results by IDs.
        :param filter_episode_id: (optional) Filter results by Episode's ID.
        :param filter_has_record_comment: (optional) Filter the results by the presence or absence of comments.
                                          If you specify `true`, only records with comments will be filtered.
                                          Specifying `false` Filter records without comments.
        :param page: (optional) Specify the number of pages.
        :param per_page: (optional) Specify how many items to acquire per page.
        :param sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param sort_likes_count: (optional) Sort the results by their number of likes. You can specify `asc` or `desc`.
        :return: List of `Record` objects.

        """
        api_method = APIMethod(
            api=self,
            path='records',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_episode_id', 'filter_has_record_comment',
                            'page', 'per_page', 'sort_id', 'sort_likes_count'),
            payload_type='record',
            payload_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def search_users(self, fields=None, filter_ids=None, filter_usernames=None,
                     page=None, per_page=None,
                     sort_id=None):
        """Get users information

        :reference: https://docs.annict.com/ja/api/v1/users.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :param filter_ids: (optional) Filter results by IDs.
        :param filter_usernames: (optional) Filter results by usernames.
        :param page: (optional) Specify the number of pages.
        :param per_page: (optional) Specify how many items to acquire per page.
        :param sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: List of `User` objects.

        """
        api_method = APIMethod(
            api=self,
            path='users',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_usernames', 'page', 'per_page', 'sort_id'),
            payload_type='user',
            payload_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def following(self, fields=None, filter_user_id=None, filter_username=None,
                  page=None, per_page=None,
                  sort_id=None):
        """Get following information

        :reference: https://docs.annict.com/ja/api/v1/following.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :param filter_user_id: (optional) Filter results by User's ID.
        :param filter_username: (optional) Filter results by username.
        :param page: (optional) Specify the number of pages.
        :param per_page: (optional) Specify how many items to acquire per page.
        :param sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: List of `User` objects

        """
        api_method = APIMethod(
            api=self,
            path='following',
            method='GET',
            allowed_params=('fields', 'filter_user_id', 'filter_username', 'page', 'per_page', 'sort_id'),
            payload_type='user',
            payload_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def followers(self, fields=None, filter_user_id=None, filter_username=None,
                  page=None, per_page=None,
                  sort_id=None):
        """Get followers information

        :reference: https://docs.annict.com/ja/api/v1/followers.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :param filter_user_id: (optional) Filter results by User's ID.
        :param filter_username: (optional) Filter results by username.
        :param page: (optional) Specify the number of pages.
        :param per_page: (optional) Specify how many items to acquire per page.
        :param sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: List of `User` objects

        """
        api_method = APIMethod(
            api=self,
            path='followers',
            method='GET',
            allowed_params=('fields', 'filter_user_id', 'filter_username', 'page', 'per_page', 'sort_id'),
            payload_type='user',
            payload_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def activities(self, fields=None, filter_user_id=None, filter_username=None,
                   page=None, per_page=None,
                   sort_id=None):
        """Get activities

        :reference: https://docs.annict.com/ja/api/v1/activities.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :param filter_user_id: (optional) Filter results by User's ID.
        :param filter_username: (optional) Filter results by username.
        :param page: (optional) Specify the number of pages.
        :param per_page: (optional) Specify how many items to acquire per page.
        :param sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: List of `Activity` objects

        """
        api_method = APIMethod(
            api=self,
            path='activities',
            method='GET',
            allowed_params=('fields', 'filter_user_id', 'filter_username', 'page', 'per_page', 'sort_id'),
            payload_type='activity',
            payload_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def me(self, fields=None):
        """Get your profile information

        :reference: https://docs.annict.com/ja/api/v1/me.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :return: `User` object of your user information.
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
        :param work_id: Work's ID
        :param kind: Types of status.
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

    def create_record(self, episode_id, comment=None, rating=None, share_twitter=None, share_facebook=None):
        """Create a record to the episode.

        :reference: https://docs.annict.com/ja/api/v1/me-records.html
        :param episode_id: Episode's ID
        :param comment: (optional) Comment.
        :param rating: (optional) Rating.
        :param share_twitter: (optional) Whether to share the record on Twitter.
                              You can enter true or false. If it is not specified, it will be false (not shared).
        :param share_facebook: (optional) Whether to share the record on Facebook.
                               You can enter true or false. If it is not specified, it will be false (not shared).
        :return: `Record` object.

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

    def edit_record(self, id_, comment=None, rating=None, share_twitter=None, share_facebook=None):
        """Edit the created record.

        :reference: https://docs.annict.com/ja/api/v1/me-records.html
        :param id_: Record's ID.
        :param comment: (optional) Comment.
        :param rating: (optional) Rating.
        :param share_twitter: (optional) Whether to share the record on Twitter.
                              You can enter true or false. If it is not specified, it will be false (not shared).
        :param share_facebook: (optional) Whether to share the record on Facebook.
                               You can enter true or false. If it is not specified, it will be false (not shared).
        :return: Episode object after update.

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
        :param id_: Recode's ID
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

    def my_works(self, fields=None, filter_ids=None, filter_season=None, filter_title=None, filter_status=None,
                 page=None, per_page=None,
                 sort_id=None, sort_season=None, sort_watchers_count=None):
        """Get the information of the work you are setting status.

        :reference: https://docs.annict.com/ja/api/v1/me-works.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :param filter_ids: (optional) Filter results by IDs.
        :param filter_season: (optional) Filter results by release time of season.
        :param filter_title: (optional) Filter results by title.
        :param filter_status: (optional) Filter results by status.
                              You can specify `wanna_watch`, `watching`, `watched`, `on_hold`, `stop_watching`.
        :param page: (optional) Specify the number of pages.
        :param per_page: (optional) Specify how many items to acquire per page.
        :param sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param sort_season: (optional) Sort the results by their release time of season. You can specify `asc` or `desc`.
        :param sort_watchers_count: (optional) Sort the results by their watchers count. You can specify `asc` or `desc`.
        :return: List of `Work` objects.

        """
        api_method = APIMethod(
            api=self,
            path='me/works',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_season', 'filter_title', 'filter_status',
                            'page', 'per_page', 'sort_id', 'sort_season', 'sort_watchers_count'),
            payload_type='work',
            payload_list=True,
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def my_programs(self, fields=None, filter_ids=None, filter_channel_ids=None, filter_work_ids=None,
                    filter_started_at_gt=None, filter_started_at_lt=None,
                    filter_unwatched=None, filter_rebroadcast=None,
                    page=None, per_page=None,
                    sort_id=None, sort_started_at=None):
        """Get the broadcast schedule.

        :reference: https://docs.annict.com/ja/api/v1/me-programs.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :param filter_ids: (optional) Filter results by IDs.
        :param filter_channel_ids: (optional) 
        :param filter_work_ids: (optional) 
        :param filter_started_at_gt: (optional) 
        :param filter_started_at_lt: (optional) 
        :param filter_unwatched: (optional) 
        :param filter_rebroadcast: (optional) 
        :param page: (optional) Specify the number of pages.
        :param per_page: (optional) Specify how many items to acquire per page.
        :param sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :param sort_started_at: (optional) 
        :return: List of `Program` objects.

        """
        api_method = APIMethod(
            api=self,
            path='me/programs',
            method='GET',
            allowed_params=('fields', 'filter_ids', 'filter_channel_ids', 'filter_work_ids', 'filter_started_at_gt',
                            'filter_started_at_lt', 'filter_unwatched', 'filter_rebroadcast',
                            'page', 'per_page', 'sort_id', 'sort_started_at'),
            payload_type='program',
            payload_list=True
        )
        params = api_method.build_parameters(locals())
        return api_method(params)

    def following_activities(self, fields=None, filter_actions=None, filter_muted=None,
                             page=None, per_page=None,
                             sort_id=None):
        """Get the activity of the user you are following.

        :reference: https://docs.annict.com/ja/api/v1/me-following-activities.html
        :param fields: (optional) Narrow down the fields of data contained in the response body.
        :param filter_actions: (optional) 
        :param filter_muted: (optional) 
        :param page: (optional) Specify the number of pages.
        :param per_page: (optional) Specify how many items to acquire per page.
        :param sort_id: (optional) Sort the results by their ID. You can specify `asc` or `desc`.
        :return: List of `Activity` objects.

        """
        api_method = APIMethod(
            api=self,
            path='me/following_activities',
            method='GET',
            allowed_params=('fields', 'filter_actions', 'filter_muted', 'page', 'per_page', 'sort_id'),
            payload_type='activity',
            payload_list=True
        )
        params = api_method.build_parameters(locals())
        return api_method(params)
