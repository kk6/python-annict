# python-annict
Annict API wrapper for python

[![CircleCI](https://circleci.com/gh/kk6/python-annict.svg?style=svg)](https://circleci.com/gh/kk6/python-annict)

python-annict は Python3.6 以上をサポートしています。

## インストール

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
>>> from annict.api import API
>>> annict = API('Your access token')
>>> results = annict.works(filter_title="Re:ゼロから始める異世界生活")
>>> print(results[0].title)
Re:ゼロから始める異世界生活
```

### キャッシュ

独自のキャッシュシステムは実装していませんが、[requests_cache](https://github.com/reclosedev/requests-cache) というrequests用キャッシュプラグインとの併用を強くおすすめします。

##### 使用例

```python
>>> import requests_cache
>>> # 有効期限300秒でメモリにキャッシュするよう設定
>>> requests_cache.install_cache(cache_name='annict', backend='memory', expire_after=300)
>>> # 最初のリクエストはAPIから
>>> api.me()
>>> # 300秒以内の同一リクエストはキャッシュから
>>> api.me()
```

さらに詳しい使い方は [Requests-cache 公式ドキュメント](https://requests-cache.readthedocs.io/en/latest/) を参照してください。