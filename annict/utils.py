# -*- coding: utf-8 -*-
from functools import singledispatch


@singledispatch
def stringify(arg):
    return str(arg)


@stringify.register(str)
def do_not_stringify(arg):
    return arg


@stringify.register(tuple)
@stringify.register(list)
@stringify.register(set)
def stringify_list(arg):
    return ','.join([str(o) for o in arg])


@stringify.register(bool)
def stringify_boolean(arg):
    return str(arg).lower()
