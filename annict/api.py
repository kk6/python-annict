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

    def works(self, *args, **kwargs):
        """Get works information

        :reference: https://docs.annict.com/ja/api/v1/works.html

        """
        api_method = APIMethod(
            api=self,
            path='works',
            method='GET',
            required_params=[],
            optional_params=[
                'fields', 'filter_ids', 'filter_season', 'filter_title',
                'page', 'per_page',
                'sort_id', 'sort_season', 'sort_watchers_count',
            ],
            payload_type='work',
            payload_list=True,
        )
        return api_method(*args, **kwargs)

    def episodes(self, *args, **kwargs):
        """Get episodes information

         :reference: https://docs.annict.com/ja/api/v1/episodes.html

        """
        api_method = APIMethod(
            api=self,
            path='episodes',
            method='GET',
            required_params=[],
            optional_params=[
                'fields', 'filter_ids', 'filter_work_id',
                'page', 'per_page',
                'sort_id', 'sort_sort_number'
            ],
            payload_type='episode',
            payload_list=True,
        )
        return api_method(*args, **kwargs)

    def records(self, *args, **kwargs):
        """Get records to episodes

        :reference: https://docs.annict.com/ja/api/v1/records.html

        """
        api_method = APIMethod(
            api=self,
            path='records',
            method='GET',
            required_params=[],
            optional_params=[
                'fields', 'filter_ids', 'filter_episode_id', 'filter_has_record_comment',
                'page', 'per_page',
                'sort_id', 'sort_likes_count'
            ],
            payload_type='record',
            payload_list=True,
        )
        return api_method(*args, **kwargs)

    def search_users(self, *args, **kwargs):
        """Get users information

        :reference: https://docs.annict.com/ja/api/v1/users.html

        """
        api_method = APIMethod(
            api=self,
            path='users',
            method='GET',
            required_params=[],
            optional_params=[
                'fields', 'filter_ids', 'filter_usernames',
                'page', 'per_page',
                'sort_id'
            ],
            payload_type='user',
            payload_list=True,
        )
        return api_method(*args, **kwargs)

    def following(self, *args, **kwargs):
        """Get following information

        :reference: https://docs.annict.com/ja/api/v1/following.html

        """
        api_method = APIMethod(
            api=self,
            path='following',
            method='GET',
            required_params=[],
            optional_params=[
                'fields', 'filter_user_id', 'filter_username',
                'page', 'per_page',
                'sort_id'
            ],
            payload_type='user',
            payload_list=True,
        )
        return api_method(*args, **kwargs)

    def followers(self, *args, **kwargs):
        """Get followers information

        :reference: https://docs.annict.com/ja/api/v1/followers.html

        """
        api_method = APIMethod(
            api=self,
            path='followers',
            method='GET',
            required_params=[],
            optional_params=[
                'fields', 'filter_user_id', 'filter_username',
                'page', 'per_page',
                'sort_id'
            ],
            payload_type='user',
            payload_list=True,
        )
        return api_method(*args, **kwargs)

    def activities(self, *args, **kwargs):
        """Get activities

        :reference: https://docs.annict.com/ja/api/v1/activities.html

        """
        api_method = APIMethod(
            api=self,
            path='activities',
            method='GET',
            required_params=[],
            optional_params=[
                'fields', 'filter_user_id', 'filter_username',
                'page', 'per_page',
                'sort_id'
            ],
            payload_type='activity',
            payload_list=True,
        )
        return api_method(*args, **kwargs)

    def me(self, *args, **kwargs):
        """Get your profile information

        :reference: https://docs.annict.com/ja/api/v1/me.html

        """
        api_method = APIMethod(
            api=self,
            path='me',
            method='GET',
            required_params=[],
            optional_params=['fields'],
            payload_type='user',
        )
        return api_method(*args, **kwargs)

    def set_status(self, work_id, kind):
        """Set the status of the work.

        :reference: https://docs.annict.com/ja/api/v1/me-statuses.html

        """
        api_method = APIMethod(
            api=self,
            path='me/statuses',
            method='POST',
            required_params=['work_id', 'kind'],
            optional_params=[],
        )
        return api_method(work_id=work_id, kind=kind)

    def create_record(self, *args, **kwargs):
        """Create a record to the episode.

        :reference: https://docs.annict.com/ja/api/v1/me-records.html

        """
        api_method = APIMethod(
            api=self,
            path='me/records',
            method='POST',
            required_params=['episode_id', ],
            optional_params=['comment', 'rating', 'share_twitter',
                             'share_facebook'],
            payload_type='record',
        )
        return api_method(*args, **kwargs)

    def edit_record(self, id_, *args, **kwargs):
        """Edit the created record.

        :reference: https://docs.annict.com/ja/api/v1/me-records.html

        """
        api_method = APIMethod(
            api=self,
            path='me/records',
            method='PATCH',
            target_id=id_,
            required_params=[],
            optional_params=['comment', 'rating', 'share_twitter',
                             'share_facebook'],
            payload_type='record',
        )
        return api_method(*args, **kwargs)

    def delete_record(self, id_):
        """Delete the created record.

        :reference: https://docs.annict.com/ja/api/v1/me-records.html

        """
        api_method = APIMethod(
            api=self,
            path='me/records',
            method='DELETE',
            target_id=id_,
            required_params=[],
            optional_params=[],
        )
        return api_method()

    def my_works(self, *args, **kwargs):
        """Get the information of the work you are setting status.

        :reference: https://docs.annict.com/ja/api/v1/me-works.html

        """
        api_method = APIMethod(
            api=self,
            path='me/works',
            method='GET',
            required_params=[],
            optional_params=[
                'fields', 'filter_ids', 'filter_season', 'filter_title', 'filter_status',
                'page', 'per_page',
                'sort_id', 'sort_season', 'sort_watchers_count'
            ],
            payload_type='work',
            payload_list=True,
        )
        return api_method(*args, **kwargs)

    def my_programs(self, *args, **kwargs):
        """Get the broadcast schedule.

        :reference: https://docs.annict.com/ja/api/v1/me-programs.html

        """
        api_method = APIMethod(
            api=self,
            path='me/programs',
            method='GET',
            required_params=[],
            optional_params=[
                'fields', 'filter_ids', 'filter_channel_ids', 'filter_work_ids',
                'filter_started_at_gt', 'filter_started_at_lt',
                'filter_unwatched', 'filter_rebroadcast',
                'page', 'per_page',
                'sort_id', 'sort_started_at'
            ],
            payload_type='program',
            payload_list=True
        )
        return api_method(*args, **kwargs)

    def following_activities(self, *args, **kwargs):
        """Get the activity of the user you are following.

        :reference: https://docs.annict.com/ja/api/v1/me-following-activities.html

        """
        api_method = APIMethod(
            api=self,
            path='me/following_activities',
            method='GET',
            required_params=[],
            optional_params=[
                'fields', 'filter_actions', 'filter_muted',
                'page', 'per_page',
                'sort_id'
            ],
            payload_type='activity',
            payload_list=True
        )
        return api_method(*args, **kwargs)
