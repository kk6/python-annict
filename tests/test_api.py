# -*- coding: utf-8 -*-
from urllib.parse import urlparse, parse_qs

import responses


def get_query(call_object):
    result = urlparse(call_object.request.url)
    return parse_qs(result.query)


@responses.activate
def test_works(api_factory):
    json = """
    {
      "works": [
        {
          "id": 4168,
          "title": "SHIROBAKO",
          "title_kana": "しろばこ",
          "media": "tv",
          "media_text": "TV",
          "season_name": "2014-autumn",
          "season_name_text": "2014年秋",
          "released_on": "2014-10-09",
          "released_on_about": "",
          "official_site_url": "http://shirobako-anime.com",
          "wikipedia_url": "http://ja.wikipedia.org/wiki/SHIROBAKO",
          "twitter_username": "shirobako_anime",
          "twitter_hashtag": "musani",
          "images": {
            "recommended_url": "http://shirobako-anime.com/images/ogp.jpg",
            "facebook": {
              "og_image_url": "http://shirobako-anime.com/images/ogp.jpg"
            },
            "twitter": {
              "mini_avatar_url": "https://twitter.com/shirobako_anime/profile_image?size=mini",
              "normal_avatar_url": "https://twitter.com/shirobako_anime/profile_image?size=normal",
              "bigger_avatar_url": "https://twitter.com/shirobako_anime/profile_image?size=bigger",
              "original_avatar_url": "https://twitter.com/shirobako_anime/profile_image?size=original",
              "image_url": ""
            }
          },
          "episodes_count": 24,
          "watchers_count": 1254
        }
      ],
      "total_count": 1,
      "next_page": null,
      "prev_page": null
    }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/works',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    works = api.works()
    assert works[0].title == 'SHIROBAKO'


@responses.activate
def test_works_with_fields(api_factory):
    json = """
    {
      "works": [
        {
          "id": 4168,
          "title": "SHIROBAKO"
        }
      ],
      "total_count": 1,
      "next_page": null,
      "prev_page": null
    }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/works',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    works = api.works('title')
    assert works[0].title == 'SHIROBAKO'
    assert not hasattr(works[0], 'title_kana')
    assert get_query(responses.calls[0]) == {'fields': ['title'], 'access_token': ['dummy_token']}


@responses.activate
def test_episodes(api_factory):
    json = """
    {
      "episodes": [
        {
          "id": 45,
          "number": null,
          "number_text": "第2話",
          "sort_number": 2,
          "title": "殺戮の夢幻迷宮",
          "records_count": 0,
          "record_comments_count": 0,
          "work": {
            "id": 3831,
            "title": "NEWドリームハンター麗夢",
            "title_kana": "",
            "media": "ova",
            "media_text": "OVA",
            "season_name": "1990-autumn",
            "season_name_text": "1990年秋",
            "released_on": "1990-12-16",
            "released_on_about": "",
            "official_site_url": "",
            "wikipedia_url": "",
            "twitter_username": "",
            "twitter_hashtag": "",
            "episodes_count": 2,
            "watchers_count": 10
          },
          "prev_episode": {
            "id": 44,
            "number": null,
            "number_text": "第1話",
            "sort_number": 1,
            "title": " 夢の騎士達",
            "records_count": 0,
            "record_comments_count": 0
          },
          "next_episode": null
        }
      ],
      "total_count": 1,
      "next_page": null,
      "prev_page": null
    }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/episodes',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    episodes = api.episodes()
    assert episodes[0].title == "殺戮の夢幻迷宮"


@responses.activate
def test_records(api_factory):
    json = """
    {
      "records": [
        {
          "id": 425551,
          "comment": "ゆるふわ田舎アニメかと思ったらギャグと下ネタが多めのコメディアニメだった。これはこれで。日岡さんの声良いなあ。",
          "rating": 4,
          "is_modified": false,
          "likes_count": 0,
          "comments_count": 0,
          "created_at": "2016-04-11T14:19:13.974Z",
          "user": {
            "id": 2,
            "username": "shimbaco",
            "name": "Koji Shimba",
            "description": "アニメ好きが高じてこのサービスを作りました。聖地巡礼を年に数回しています。",
            "url": "http://shimba.co",
            "avatar_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_avatars/master/d8af7adc8122c96ba7639218fd8b5ede332d42f2.jpg?1431357292",
            "background_image_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_background_images/master/ee15d577fb2f2d61bdaf700cfab894b286a5762d.jpg?1486753229",
            "records_count": 1906,
            "created_at": "2014-03-02T15:38:40.000Z"
          },
          "work": {
            "id": 4670,
            "title": "くまみこ",
            "title_kana": "くまみこ",
            "media": "tv",
            "media_text": "TV",
            "season_name": "2016-spring",
            "season_name_text": "2016年春",
            "released_on": "",
            "released_on_about": "",
            "official_site_url": "http://kmmk.tv/",
            "wikipedia_url": "https://ja.wikipedia.org/wiki/%E3%81%8F%E3%81%BE%E3%81%BF%E3%81%93",
            "twitter_username": "kmmk_anime",
            "twitter_hashtag": "kumamiko",
            "episodes_count": 6,
            "watchers_count": 609
          },
          "episode": {
            "id": 74669,
            "number": "1",
            "number_text": "第壱話",
            "sort_number": 10,
            "title": "クマと少女 お別れの時",
            "records_count": 183,
            "record_comments_count": 53
          }
        }
      ],
      "total_count": 1,
      "next_page": null,
      "prev_page": null
    }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/records',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    records = api.records(filter_episode_id=74669)
    assert records[0].comment.startswith("ゆるふわ田舎アニメかと思ったら")
    assert get_query(responses.calls[0]) == {'filter_episode_id': ['74669'], 'access_token': ['dummy_token']}


@responses.activate
def test_users(api_factory):
    json = """
        {
          "users": [
            {
              "id": 2,
              "username": "shimbaco",
              "name": "Koji Shimba",
              "description": "アニメ好きが高じてこのサービスを作りました。聖地巡礼を年に数回しています。",
              "url": "http://shimba.co",
              "avatar_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_avatars/master/d8af7adc8122c96ba7639218fd8b5ede332d42f2.jpg?1431357292",
              "background_image_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_background_images/master/ee15d577fb2f2d61bdaf700cfab894b286a5762d.jpg?1486753229",
              "records_count": 2369,
              "created_at": "2014-03-02T15:38:40.000Z"
            }
          ],
          "total_count": 1,
          "next_page": null,
          "prev_page": null
        }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/users',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    users = api.search_users(filter_usernames='shimbaco')
    assert users[0].name == 'Koji Shimba'
    assert get_query(responses.calls[0]) == {'filter_usernames': ['shimbaco'], 'access_token': ['dummy_token']}


@responses.activate
def test_following(api_factory):
    json = """
        {
          "users": [
            {
              "id": 3,
              "username": "builtlast",
              "name": "岩永勇輝 (Creasty)",
              "description": "Web やってる大学生\\nプログラミングとかデザインとか\\n価値を生み出せるようになりたい\\n\\nアルバイト@FICC\\n\\nC / Obj-C / Ruby / Haskell / PHP / CoffeeScript / VimScript / Photoshop / Illustrator",
              "url": null,
              "avatar_url": "https://api-assets.annict.com/paperclip/profiles/2/tombo_avatars/master/cc301ca5c5e13399144c79daa4e4727b783676de.jpg?1428129519",
              "background_image_url": "https://api-assets.annict.com/paperclip/profiles/2/tombo_avatars/master/cc301ca5c5e13399144c79daa4e4727b783676de.jpg?1428129519",
              "records_count": 0,
              "created_at": "2014-03-04T09:32:25.000Z"
            },
            {
              "id": 4,
              "username": "pataiji",
              "name": "PATAIJI",
              "description": "FICC inc.ベースやってます。カブに乗ってます。AWSすごい良い。Railsすごい楽。",
              "url": null,
              "avatar_url": "https://api-assets.annict.com/paperclip/profiles/3/tombo_avatars/master/33ce537a4cf38f71b509f295f2afa3291c281dcf.jpg?1428129521",
              "background_image_url": "https://api-assets.annict.com/paperclip/profiles/3/tombo_avatars/master/33ce537a4cf38f71b509f295f2afa3291c281dcf.jpg?1428129521",
              "records_count": 0,
              "created_at": "2014-03-04T09:32:28.000Z"
            }
          ],
          "total_count": 274,
          "next_page": 2,
          "prev_page": null
        }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/following',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    following = api.following(filter_username='shimbaco', per_page=2)
    assert following[0].username == 'builtlast'
    assert get_query(responses.calls[0]) == {'filter_username': ['shimbaco'], 'per_page': ['2'],
                                             'access_token': ['dummy_token']}


@responses.activate
def test_followers(api_factory):
    json = """
        {
          "users": [
            {
              "id": 7,
              "username": "akirafukuoka",
              "name": "akirafukuoka",
              "description": "FICC inc. http://www.ficc.jp  クリエイティブディレクター。RAW-Fi http://raw-fi.com  @raw_fi もよろしくお願いします。",
              "url": null,
              "avatar_url": "https://api-assets.annict.com/paperclip/profiles/6/tombo_avatars/master/480862747fc5f7152a031e24f0c0374dc71c539a.jpg?1431596794",
              "background_image_url": "https://api-assets.annict.com/paperclip/profiles/6/tombo_background_images/master/7e258e0189e9ee38f4dc0c57b2c9f6b39dd2cd95.jpg?1431596795",
              "records_count": 260,
              "created_at": "2014-03-10T04:11:54.000Z"
            },
            {
              "id": 8,
              "username": "310u8",
              "name": "Daisuke Nagai",
              "description": "歌って踊れるWebデザイナーです",
              "url": null,
              "avatar_url": "https://api-assets.annict.com/paperclip/profiles/7/tombo_avatars/master/cd7b66919fea1952e63855632665812839e2a394.jpg?1428129527",
              "background_image_url": "https://api-assets.annict.com/paperclip/profiles/7/tombo_avatars/master/cd7b66919fea1952e63855632665812839e2a394.jpg?1428129527",
              "records_count": 739,
              "created_at": "2014-03-10T04:11:55.000Z"
            }
          ],
          "total_count": 191,
          "next_page": 2,
          "prev_page": null
        }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/followers',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    followers = api.followers()
    assert followers[0].username == 'akirafukuoka'


@responses.activate
def test_activities(api_factory):
    json = """
        {
          "activities": [
            {
              "id": 1504708,
              "user": {
                "id": 2,
                "username": "shimbaco",
                "name": "Koji Shimba",
                "description": "アニメ好きが高じてこのサービスを作りました。聖地巡礼を年に数回しています。",
                "url": "http://shimba.co",
                "avatar_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_avatars/master/d8af7adc8122c96ba7639218fd8b5ede332d42f2.jpg?1431357292",
                "background_image_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_background_images/master/ee15d577fb2f2d61bdaf700cfab894b286a5762d.jpg?1486753229",
                "records_count": 2369,
                "created_at": "2014-03-02T15:38:40.000Z"
              },
              "action": "create_record",
              "created_at": "2017-02-22T13:24:44.761Z",
              "work": {
                "id": 5036,
                "title": "小林さんちのメイドラゴン",
                "title_kana": "こばやしさんちのめいどらごん",
                "media": "tv",
                "media_text": "TV",
                "released_on": "",
                "released_on_about": "",
                "official_site_url": "http://maidragon.jp/",
                "wikipedia_url": "https://ja.wikipedia.org/wiki/%E5%B0%8F%E6%9E%97%E3%81%95%E3%82%93%E3%81%A1%E3%81%AE%E3%83%A1%E3%82%A4%E3%83%89%E3%83%A9%E3%82%B4%E3%83%B3",
                "twitter_username": "maidragon_anime",
                "twitter_hashtag": "maidragon",
                "episodes_count": 7,
                "watchers_count": 448,
                "season_name": "2017-winter",
                "season_name_text": "2017年冬"
              },
              "episode": {
                "id": 89678,
                "number": "6",
                "number_text": "#6",
                "sort_number": 60,
                "title": "お宅訪問！(してないお宅もあります)",
                "records_count": 89,
                "record_comments_count": 24
              },
              "record": {
                "id": 864718,
                "comment": "",
                "rating": null,
                "is_modified": false,
                "likes_count": 0,
                "comments_count": 0,
                "created_at": "2017-02-22T13:24:39.353Z"
              }
            }
          ],
          "total_count": 3705,
          "next_page": 2,
          "prev_page": null
        }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/activities',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    activities = api.activities()
    assert activities[0].id == 1504708


@responses.activate
def test_me(api_factory):
    json = """
        {
          "id": 2,
          "username": "shimbaco",
          "name": "Koji Shimba",
          "description": "アニメ好きが高じてこのサービスを作りました。聖地巡礼を年に数回しています。",
          "url": "http://shimba.co",
          "avatar_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_avatars/master/d8af7adc8122c96ba7639218fd8b5ede332d42f2.jpg?1431357292",
          "background_image_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_background_images/master/ee15d577fb2f2d61bdaf700cfab894b286a5762d.jpg?1486753229",
          "records_count": 2369,
          "created_at": "2014-03-02T15:38:40.000Z",
          "email": "me@shimba.co",
          "notifications_count": 0
        }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/me',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    me = api.me()
    assert me.username == 'shimbaco'


@responses.activate
def test_set_status(api_factory):
    responses.add(responses.POST, 'https://api.annict.com/v1/me/statuses',
                  body=None, status=204)
    api = api_factory.create()
    result = api.set_status(work_id=438, kind='watching')
    assert result is True


@responses.activate
def test_create_record(api_factory):
    json = """
        {
          "id": 470491,
          "comment": "あぁ^～心がぴょんぴょんするんじゃぁ^～",
          "rating": null,
          "is_modified": false,
          "likes_count": 0,
          "comments_count": 0,
          "created_at": "2016-05-07T09:40:32.159Z",
          "user": {
            "id": 2,
            "username": "shimbaco",
            "name": "Koji Shimba",
            "description": "",
            "url": null,
            "avatar_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_avatars/master/d8af7adc8122c96ba7639218fd8b5ede332d42f2.jpg?1431357292",
            "background_image_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_background_images/master/ee15d577fb2f2d61bdaf700cfab894b286a5762d.jpg?1486753229",
            "records_count": 123,
            "created_at": "2016-05-03T19:06:59.929Z"
          },
          "work": {
            "id": 3994,
            "title": "ご注文はうさぎですか？",
            "title_kana": "ごちゅうもんはうさぎですか",
            "media": "tv",
            "media_text": "TV",
            "season_name": "2014-spring",
            "season_name_text": "2014年春",
            "released_on": "2014-04-10",
            "released_on_about": "",
            "official_site_url": "http://www.gochiusa.com/",
            "wikipedia_url": "http://ja.wikipedia.org/wiki/%E3%81%94%E6%B3%A8%E6%96%87%E3%81%AF%E3%81%86%E3%81%95%E3%81%8E%E3%81%A7%E3%81%99%E3%81%8B%3F#.E3.83.86.E3.83.AC.E3.83.93.E3.82.A2.E3.83.8B.E3.83.A1",
            "twitter_username": "usagi_anime",
            "twitter_hashtag": "gochiusa",
            "episodes_count": 12,
            "watchers_count": 850
          },
          "episode": {
            "id": 5013,
            "number": null,
            "number_text": "第1羽",
            "sort_number": 1,
            "title": "ひと目で尋常でないもふもふだと見抜いたよ",
            "records_count": 103,
            "record_comments_count": 3
          }
        }
    """
    responses.add(responses.POST, 'https://api.annict.com/v1/me/records',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    record = api.create_record(episode_id=5013, comment="あぁ^～心がぴょんぴょんするんじゃぁ^～")
    assert record.comment == "あぁ^～心がぴょんぴょんするんじゃぁ^～"


@responses.activate
def test_edit_record(api_factory):
    json = """
        {
          "id": 1016,
          "comment": "あぁ^～心がぴょんぴょんするんじゃぁ^～",
          "rating": 5.0,
          "is_modified": true,
          "likes_count": 0,
          "comments_count": 0,
          "created_at": "2016-05-07T09:40:32.159Z",
          "user": {
            "id": 2,
            "username": "shimbaco",
            "name": "Koji Shimba",
            "description": "",
            "url": null,
            "avatar_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_avatars/master/d8af7adc8122c96ba7639218fd8b5ede332d42f2.jpg?1431357292",
            "background_image_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_background_images/master/ee15d577fb2f2d61bdaf700cfab894b286a5762d.jpg?1486753229",
            "records_count": 1234,
            "created_at": "2016-05-03T19:06:59.929Z"
          },
          "work": {
            "id": 3994,
            "title": "ご注文はうさぎですか？",
            "title_kana": "ごちゅうもんはうさぎですか",
            "media": "tv",
            "media_text": "TV",
            "season_name": "2014-spring",
            "season_name_text": "2014年春",
            "released_on": "2014-04-10",
            "released_on_about": "",
            "official_site_url": "http://www.gochiusa.com/",
            "wikipedia_url": "http://ja.wikipedia.org/wiki/%E3%81%94%E6%B3%A8%E6%96%87%E3%81%AF%E3%81%86%E3%81%95%E3%81%8E%E3%81%A7%E3%81%99%E3%81%8B%3F#.E3.83.86.E3.83.AC.E3.83.93.E3.82.A2.E3.83.8B.E3.83.A1",
            "twitter_username": "usagi_anime",
            "twitter_hashtag": "gochiusa",
            "episodes_count": 12,
            "watchers_count": 850
          },
          "episode": {
            "id": 5013,
            "number": null,
            "number_text": "第1羽",
            "sort_number": 1,
            "title": "ひと目で尋常でないもふもふだと見抜いたよ",
            "records_count": 103,
            "record_comments_count": 3
          }
        }
    """
    responses.add(responses.PATCH, 'https://api.annict.com/v1/me/records/1016',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    record = api.edit_record(1016, comment="あぁ^～心がぴょんぴょんするんじゃぁ^～",
                             rating=5.0, share_facebook=True)
    assert record.rating == 5.0


@responses.activate
def test_delete_record(api_factory):
    responses.add(responses.DELETE, 'https://api.annict.com/v1/me/records/1016',
                  body=None, status=204)
    api = api_factory.create()
    result = api.delete_record(1016)
    assert result is True


@responses.activate
def test_my_works(api_factory):
    json = """
        {
          "works": [
            {
              "id": 4681,
              "title": "ふらいんぐうぃっち",
              "title_kana": "ふらいんぐうぃっち",
              "media": "tv",
              "media_text": "TV",
              "season_name": "2016-spring",
              "season_name_text": "2016年春",
              "released_on": "",
              "released_on_about": "",
              "official_site_url": "http://www.flyingwitch.jp/",
              "wikipedia_url": "https://ja.wikipedia.org/wiki/%E3%81%B5%E3%82%89%E3%81%84%E3%82%93%E3%81%90%E3%81%86%E3%81%83%E3%81%A3%E3%81%A1",
              "twitter_username": "flying_tv",
              "twitter_hashtag": "flyingwitch",
              "episodes_count": 5,
              "watchers_count": 695,
              "status": {
                "kind": "watching"
              }
            }
          ],
          "total_count": 1,
          "next_page": null,
          "prev_page": null
        }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/me/works',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    works = api.my_works()
    assert works[0].title == "ふらいんぐうぃっち"


@responses.activate
def test_my_programs(api_factory):
    json = """
        {
          "programs": [
            {
              "id": 35387,
              "started_at": "2016-05-07T20:10:00.000Z",
              "is_rebroadcast": false,
              "channel": {
                "id": 4,
                "name": "日本テレビ"
              },
              "work": {
                "id": 4681,
                "title": "ふらいんぐうぃっち",
                "title_kana": "ふらいんぐうぃっち",
                "media": "tv",
                "media_text": "TV",
                "season_name": "2016-spring",
                "season_name_text": "2016年春",
                "released_on": "",
                "released_on_about": "",
                "official_site_url": "http://www.flyingwitch.jp/",
                "wikipedia_url": "https://ja.wikipedia.org/wiki/%E3%81%B5%E3%82%89%E3%81%84%E3%82%93%E3%81%90%E3%81%86%E3%81%83%E3%81%A3%E3%81%A1",
                "twitter_username": "flying_tv",
                "twitter_hashtag": "flyingwitch",
                "episodes_count": 5,
                "watchers_count": 695
              },
              "episode": {
                "id": 75187,
                "number": "5",
                "number_text": "第5話",
                "sort_number": 50,
                "title": "使い魔の活用法",
                "records_count": 0,
                "record_comments_count": 0
              }
            }
          ],
          "total_count": 1,
          "next_page": null,
          "prev_page": null
        }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/me/programs',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    programs = api.my_programs(sort_started_at='desc', filter_started_at_gt='2016/05/05 02:00')
    assert programs[0].id == 35387
    assert get_query(responses.calls[0]) == {'sort_started_at': ['desc'], 'filter_started_at_gt': ['2016/05/05 02:00'],
                                             'access_token': ['dummy_token']}


@responses.activate
def test_following_activities(api_factory):
    json = """
        {
          "activities": [
            {
              "id": 1504708,
              "user": {
                "id": 2,
                "username": "shimbaco",
                "name": "Koji Shimba",
                "description": "アニメ好きが高じてこのサービスを作りました。聖地巡礼を年に数回しています。",
                "url": "http://shimba.co",
                "avatar_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_avatars/master/d8af7adc8122c96ba7639218fd8b5ede332d42f2.jpg?1431357292",
                "background_image_url": "https://api-assets.annict.com/paperclip/profiles/1/tombo_background_images/master/ee15d577fb2f2d61bdaf700cfab894b286a5762d.jpg?1486753229",
                "records_count": 2369,
                "created_at": "2014-03-02T15:38:40.000Z"
              },
              "action": "create_record",
              "created_at": "2017-02-22T13:24:44.761Z",
              "work": {
                "id": 5036,
                "title": "小林さんちのメイドラゴン",
                "title_kana": "こばやしさんちのめいどらごん",
                "media": "tv",
                "media_text": "TV",
                "released_on": "",
                "released_on_about": "",
                "official_site_url": "http://maidragon.jp/",
                "wikipedia_url": "https://ja.wikipedia.org/wiki/%E5%B0%8F%E6%9E%97%E3%81%95%E3%82%93%E3%81%A1%E3%81%AE%E3%83%A1%E3%82%A4%E3%83%89%E3%83%A9%E3%82%B4%E3%83%B3",
                "twitter_username": "maidragon_anime",
                "twitter_hashtag": "maidragon",
                "episodes_count": 7,
                "watchers_count": 448,
                "season_name": "2017-winter",
                "season_name_text": "2017年冬"
              },
              "episode": {
                "id": 89678,
                "number": "6",
                "number_text": "#6",
                "sort_number": 60,
                "title": "お宅訪問！(してないお宅もあります)",
                "records_count": 89,
                "record_comments_count": 24
              },
              "record": {
                "id": 864718,
                "comment": "",
                "rating": null,
                "is_modified": false,
                "likes_count": 0,
                "comments_count": 0,
                "created_at": "2017-02-22T13:24:39.353Z"
              }
            }
          ],
          "total_count": 138030,
          "next_page": 2,
          "prev_page": null
        }
    """
    responses.add(responses.GET, 'https://api.annict.com/v1/me/following_activities',
                  body=json, status=200,
                  content_type='application/json')
    api = api_factory.create()
    activities = api.following_activities(sort_id='desc', per_page=1)
    assert activities[0].id == 1504708
    assert get_query(responses.calls[0]) == {'sort_id': ['desc'], 'per_page': ['1'], 'access_token': ['dummy_token']}
