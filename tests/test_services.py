# -*- coding: utf-8 -*-
import pytest


class TestBuildParameters:

    def _make_one(self, allowed_params, client=None, parser=None):
        from annict.services import ServiceBase
        sb = ServiceBase(client, parser)
        sb.allowed_params = allowed_params
        return sb

    def test_ok_with_args(self):
        sb = self._make_one(['a', 'b', 'c'])
        params = sb.build_parameters((1, 2, 3), {})
        assert params == {'a': '1', 'b': '2', 'c': '3'}

    def test_ok_with_kwargs(self):
        sb = self._make_one(['a', 'b', 'c'])
        params = sb.build_parameters((), {'a': 1, 'b': 2, 'c': 3})
        assert params == {'a': '1', 'b': '2', 'c': '3'}

    def test_ok_with_both(self):
        sb = self._make_one(['a', 'b', 'c'])
        params = sb.build_parameters((1, 2), {'c': 3})
        assert params == {'a': '1', 'b': '2', 'c': '3'}

    def test_too_many_parameter_supplied_then_causes_exception(self):
        from annict.exceptions import AnnictError
        sb = self._make_one([])
        with pytest.raises(AnnictError) as exc_info:
            params = sb.build_parameters([1, 2, 3], {})
        assert str(exc_info.value) == "Too many parameters supplied."

    def test_passing_unknown_keyword_then_causes_exception(self):
        from annict.exceptions import AnnictError
        sb = self._make_one(['a', 'b', 'c'])
        with pytest.raises(AnnictError) as exc_info:
            params = sb.build_parameters((), {'a': 1, 'b': 2, 'c': 3, 'd': 4})
        assert str(exc_info.value) == "Unknown keyword supplied: 'd'"

    def test_multiple_keyword_value_supplied_then_causes_exception(self):
        from annict.exceptions import AnnictError
        sb = self._make_one(['a', 'b', 'c'])
        with pytest.raises(AnnictError) as exc_info:
            params = sb.build_parameters((10,), {'a': 1, 'b': 2, 'c': 3})
        assert str(exc_info.value) == "Multiple values for parameter 'a' supplied."
