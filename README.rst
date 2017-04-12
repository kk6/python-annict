python-annict
=============

`Annict API <https://docs.annict.com/ja/api/>`__ wrapper for Python

|CircleCI| |PyPI|

**python-annict** officially supports Python 3.6.

Installation
------------

.. code:: bash

    $ pip install annict

Quickstart
----------

Authentication
~~~~~~~~~~~~~~

Acquire the URL for authentication code.

.. code:: python

    >>> from annict.auth import OAuthHandler
    >>> handler = OAuthHandler(client_id='Your client ID', client_secret='Your client secret')
    >>> url = handler.get_authorization_url(scope='read write')
    >>> print(url)

Open the browser and access the URL you obtained, the authentication
code will be displayed. It will be passed to the
``handler.authenticate()`` 's argument to get the access token.

.. code:: python

    >>> handler.authenticate(code='Authentication code')
    >>> print(handler.get_access_token())

Note that this authentication flow is unnecessary when issuing a
personal access token on Annict and using it.

See: `Annict API:
個人用アクセストークンが発行できるようになりました <http://blog.annict.com/post/157138114218/personal-access-token>`__

Hello world
~~~~~~~~~~~

.. code:: python

    >>> from annict.api import API
    >>> annict = API('Your access token')
    >>> results = annict.works(filter_title="Re:ゼロから始める異世界生活")
    >>> print(results[0].title)
    Re:ゼロから始める異世界生活

Cache
~~~~~

For now, we do not have our own cache system. However, caching is also
important to reduce the load on AnnictAPI.

So I introduce a cache plugin for *requests* library called
`requests\_cache <https://github.com/reclosedev/requests-cache>`__.

Install with pip.

.. code:: bash

    $ pip insall requests_cache

*requests\_cache* is very easy to use.

.. code:: python

    >>> import requests_cache
    >>> requests_cache.install_cache(cache_name='annict', backend='memory', expire_after=300)
    >>> # At first, from Annict API.
    >>> api.me()
    >>> # You can get results from cache, if it is within the expiration time.
    >>> api.me()

For more information: `Requests-cache
documentation <https://requests-cache.readthedocs.io/en/latest/>`__

.. |CircleCI| image:: https://img.shields.io/circleci/project/kk6/python-annict.svg?style=flat-square
   :target: https://circleci.com/gh/kk6/python-annict
.. |PyPI| image:: https://img.shields.io/pypi/v/annict.svg?style=flat-square
   :target: https://pypi.python.org/pypi/annict
