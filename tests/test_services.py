# -*- coding: utf-8 -*-
import pytest


class TestBuildParameters:

    def _make_one(self, required_params=list(), optional_params=list()):
        from annict.services import APIMethod

        class DummyAPI:
            token = 'dummy_token'
        api_method = APIMethod(api=DummyAPI(), path='path/to', method='GET',
                               required_params=required_params, optional_params=optional_params)
        return api_method

    def test_ok_with_args(self):
        api_method = self._make_one(['a', 'b', 'c'])
        params = api_method.build_parameters((1, 2, 3), {})
        assert params == {'a': '1', 'b': '2', 'c': '3'}

    def test_ok_with_kwargs(self):
        api_method = self._make_one(['a', 'b', 'c'])
        params = api_method.build_parameters((), {'a': 1, 'b': 2, 'c': 3})
        assert params == {'a': '1', 'b': '2', 'c': '3'}

    def test_ok_with_both(self):
        api_method = self._make_one(['a', 'b', 'c'])
        params = api_method.build_parameters((1, 2), {'c': 3})
        assert params == {'a': '1', 'b': '2', 'c': '3'}

    def test_too_many_parameter_supplied_then_causes_exception(self):
        from annict.exceptions import AnnictError
        api_method = self._make_one([])
        with pytest.raises(AnnictError) as exc_info:
            api_method.build_parameters([1, 2, 3], {})
        assert str(exc_info.value) == "Too many parameters supplied."

    def test_passing_unknown_keyword_then_causes_exception(self):
        from annict.exceptions import AnnictError
        api_method = self._make_one(['a', 'b', 'c'])
        with pytest.raises(AnnictError) as exc_info:
            api_method.build_parameters((), {'a': 1, 'b': 2, 'c': 3, 'd': 4})
        assert str(exc_info.value) == "Unknown keyword supplied: 'd'"

    def test_multiple_keyword_value_supplied_then_causes_exception(self):
        from annict.exceptions import AnnictError
        api_method = self._make_one(['a', 'b', 'c'])
        with pytest.raises(AnnictError) as exc_info:
            api_method.build_parameters((10,), {'a': 1, 'b': 2, 'c': 3})
        assert str(exc_info.value) == "Multiple values for parameter 'a' supplied."
