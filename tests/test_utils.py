# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize(
    "arg,expected",
    [
        ("string", "string"),
        (1, "1"),
        (4.5, "4.5"),
        ([1, 2], "1,2"),
        ((2, 3), "2,3"),
        ({4, 5}, "4,5"),
    ],
)
def test_stringify(arg, expected):
    from annict.utils import stringify

    assert stringify(arg) == expected
