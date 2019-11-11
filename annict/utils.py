# -*- coding: utf-8 -*-
from functools import singledispatch
from typing import Any


@singledispatch
def stringify(arg: Any) -> str:
    return str(arg)


@stringify.register(str)
def do_not_stringify(arg: str) -> str:
    return arg


@stringify.register(tuple)
@stringify.register(list)
@stringify.register(set)
def stringify_list(arg: Any) -> str:
    return ",".join([str(o) for o in arg])


@stringify.register(bool)
def stringify_boolean(arg: bool) -> str:
    return str(arg).lower()
