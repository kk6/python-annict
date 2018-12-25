# python-annict

[Annict API](https://docs.annict.com/ja/api/) wrapper for Python

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e7936cf6e72a4e14b3bfb07879de1c3d)](https://app.codacy.com/app/hiro.ashiya/python-annict?utm_source=github.com&utm_medium=referral&utm_content=kk6/python-annict&utm_campaign=Badge_Grade_Dashboard)
[![CircleCI](https://img.shields.io/circleci/project/github/kk6/python-annict.svg?style=flat-square)](https://circleci.com/gh/kk6/python-annict)
[![PyPI](https://img.shields.io/pypi/v/annict.svg?style=flat-square)](https://pypi.org/project/annict/)
[![License](https://img.shields.io/pypi/l/annict.svg)](https://pypi.org/project/annict/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

**python-annict** officially supports Python 3.6 or higher.

## Installation

```bash
pip install annict
```

## Quickstart

### Authentication

Acquire the URL for authentication code.

```python
>>> from annict.auth import OAuthHandler
>>> handler = OAuthHandler(client_id='Your client ID', client_secret='Your client secret')
>>> url = handler.get_authorization_url(scope='read write')
>>> print(url)
```

Open the browser and access the URL you obtained, the authentication code will be displayed.
It will be passed to the `handler.authenticate()` 's argument to get the access token.

```python
>>> handler.authenticate(code='Authentication code')
>>> print(handler.get_access_token())
```

Note that this authentication flow is unnecessary when issuing a personal access token on Annict and using it.

See: [Annict API: 個人用アクセストークンが発行できるようになりました](http://blog.annict.com/post/157138114218/personal-access-token)

### Hello world


```python
>>> from annict.api import API
>>> annict = API('Your access token')
>>> results = annict.works(filter_title="Re:ゼロから始める異世界生活")
>>> print(results[0].title)
Re:ゼロから始める異世界生活
```

### Cache

For now, we do not have our own cache system. However, caching is also important to reduce the load on AnnictAPI.

So I introduce a cache plugin for *requests* library called [requests_cache](https://github.com/reclosedev/requests-cache).

Install with pip.

```bash
pip insall requests_cache
```

*requests_cache* is very easy to use.

```python
>>> import requests_cache
>>> requests_cache.install_cache(cache_name='annict', backend='memory', expire_after=300)
>>> # At first, from Annict API.
>>> api.me()
>>> # You can get results from cache, if it is within the expiration time.
>>> api.me()

```

For more information: [Requests-cache documentation](https://requests-cache.readthedocs.io/en/latest/) 

## Documentation

- [This library's documentation](https://pythonhosted.org/annict/)
- [Annict Docs(Japanese)](https://docs.annict.com/ja/)
