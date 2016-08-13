# python-annict
Annict API wrapper for python

## 使い方

### 認証

認証コード取得用のURLを生成

```python
>>> from annict.auth import OAuthHandler
>>> handler = OAuthHandler(client_id='Your client ID', client_secret='Your client secret')
>>> url = handler.get_authorization_url(scope='read write')
>>> print(url)
```

URLをブラウザで開いて認証コードを表示します。それを `handler.authenticate()` の引数に渡してアクセストークンを取得します。

```python
>>> handler.authenticate(code='Authentication code')
>>> print(handler.get_access_token())
```

### API


```python
>>> from annict.api import Api
>>> annict = Api('Your access token')
>>> results = annict.works(filter_title="Re:ゼロから始める異世界生活")
>>> print(results[0])
```
