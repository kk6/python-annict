# -*- coding: utf-8 -*-
from functools import wraps


class SimpleCursor(object):
    """Simple cursor class"""

    def __init__(self, method, **kwargs):
        if not hasattr(method, 'cursor_support'):
            raise TypeError(f"Cursor does not support this method: {method.__func__.__qualname__}")
        self.method = method
        self.kwargs = kwargs
        if 'page' not in self.kwargs:
            self.kwargs['page'] = 1

    def cursor(self):
        while 1:
            results = self.method(**self.kwargs)
            for result in results:
                yield result
            self.kwargs['page'] += 1
            if not results.next_page or not results:
                return


def cursor_support(api_method):
    """
    Cursor support decorator

    :param api_method: API method that wan to correspond to the cursor.
    :return: wrapped method

    """
    api_method.cursor_support = True

    @wraps(api_method)
    def wrapper(*args, **kwargs):
        return api_method(*args, **kwargs)
    return wrapper
