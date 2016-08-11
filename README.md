# python-annict
Annict API wrappeer for python

## Usage

### OAuth

First, to get the authentication code.

```python
>>> from annict.auth import AnnictOAuthHandler
>>> handler = AnnictOAuthHandler(client_id='Your client ID', client_secret='Your client secret')
>>> handler.authorize(scope='read write')
True
```

Here in the browser, which opens the page the authentication code is displayed. After you copy the authentication code, and passes it to authenticate method as an argument.

```python
>>> session = handler.authenticate(code='Authentication code')
>>> print(session.access_token)
```
