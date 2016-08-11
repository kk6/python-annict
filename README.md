# python-annict
Annict API wrappeer for python

## Usage

### Authentication

First, to get the authentication code.

```python
>>> from annict.auth import OAuthHandler
>>> handler = OAuthHandler(client_id='Your client ID', client_secret='Your client secret')
>>> url = handler.get_authorization_url(scope='read write')
>>> print(url)
```


When you open this URL in your browser, authentication code is displayed. After you copy the authentication code, and passes it to authenticate method as an argument.

```python
>>> handler.authenticate(code='Authentication code')
>>> print(handler.get_access_token())
```
