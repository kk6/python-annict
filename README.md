# python-annict
Annict API wrappeer for python

## Usage

### OAuth

First, to get the authentication code.

```python
>>> from annict.auth import AnnictOAuthHandler
>>> handler = AnnictOAuthHandler(client_id='Your client ID', client_secret='Your client secret')
>>> url = handler.get_authorize_url(scope='read write')
>>> print(url)
```


When you open this URL in your browser, authentication code is displayed. After you copy the authentication code, and passes it to authenticate method as an argument.

```python
>>> session = handler.authenticate(code='Authentication code')
>>> print(session.access_token)
```
