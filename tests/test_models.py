# -*- coding: utf-8 -*-
import datetime
from arrow import arrow

tzutc = arrow.dateutil_tz.tzutc


def test_user():
    from annict.models import User
    json = {
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
    user = User.parse(None, json)
    assert user.id == 2
    assert user.username == "shimbaco"
    assert user.name == "Koji Shimba"
    assert user.description == "アニメ好きが高じてこのサービスを作りました。聖地巡礼を年に数回しています。"
    assert user.url == "http://shimba.co"
    assert user.avatar_url == "https://api-assets.annict.com/paperclip/profiles/1/tombo_avatars/master/d8af7adc8122c96ba7639218fd8b5ede332d42f2.jpg?1431357292"
    assert user.background_image_url == "https://api-assets.annict.com/paperclip/profiles/1/tombo_background_images/master/ee15d577fb2f2d61bdaf700cfab894b286a5762d.jpg?1486753229"
    assert user.records_count == 2369
    assert user.created_at == datetime.datetime(2014, 3, 2, 15, 38, 40, tzinfo=tzutc())
    assert user.email == "me@shimba.co"
    assert user.notifications_count == 0


def test_work():
    json = {
        'episodes_count': 21,
        'id': 4636,
        'media': 'tv',
        'media_text': 'TV',
        'official_site_url': 'http://re-zero-anime.jp/',
        'released_on': '2016-04-03',
        'released_on_about': '',
        'season_name': '2016-spring',
        'season_name_text': '2016年春',
        'title': 'Re:ゼロから始める異世界生活',
        'title_kana': 'りぜろからはじめるいせかいせいかつ',
        'twitter_hashtag': 'rezero',
        'twitter_username': 'Rezero_official',
        'watchers_count': 970,
        'wikipedia_url': ('https://ja.wikipedia.org/wiki/Re:%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E5'
                          '%A7%8B%E3%82%81%E3%82%8B%E7%95%B0%E4%B8%96%E7%95%8C%E7%94%9F%E6%B4%BB'),
    }
    from annict.models import Work

    work = Work.parse('dummy_api', json)

    assert work.id == 4636
    assert work.title == 'Re:ゼロから始める異世界生活'
    assert work.released_on == datetime.date(2016, 4, 3)


def test_episode():
    json = {
        "id": 45,
        "number": None,
        "number_text": "第2話",
        "sort_number": 2,
        "title": "殺戮の夢幻迷宮",
        "records_count": 0,
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
            "number": None,
            "number_text": "第1話",
            "sort_number": 1,
            "title": " 夢の騎士達",
            "records_count": 0
        },
        "next_episode": None
    }
    from annict.models import Episode

    episode = Episode.parse(None, json)

    assert episode.id == 45
    assert episode.work.id == 3831
    assert episode.prev_episode.id == 44
    assert episode.next_episode is None


def test_record():
    json = {
        "id": 425551,
        "comment": "ゆるふわ田舎アニメかと思ったらギャグと下ネタが多めのコメディアニメだった。これはこれで。日岡さんの声良いなあ。",
        "rating": 4,
        "is_modified": False,
        "likes_count": 0,
        "comments_count": 0,
        "created_at": "2016-04-11T14:19:13.974Z",
        "user": {
            "id": 2,
            "username": "shimbaco",
            "name": "Koji Shimba",
            "description": "アニメ好きが高じてこのサービスを作りました。聖地巡礼を年に数回しています。",
            "url": "http://shimba.co",
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
            "records_count": 183
        }
    }

    from annict.models import Record

    record = Record.parse(None, json)

    assert record.id == 425551
    assert record.user.id == 2
    assert record.work.id == 4670
    assert record.episode.id == 74669
    assert record.created_at == datetime.datetime(2016, 4, 11, 14, 19, 13, 974000, tzinfo=tzutc())


def test_program():
    json = {
        "id": 35387,
        "started_at": "2016-05-07T20:10:00.000Z",
        "is_rebroadcast": False,
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
            "records_count": 0
        }
    }

    from annict.models import Program

    program = Program.parse(None, json)

    assert program.id == 35387
    assert program.started_at == datetime.datetime(2016, 5, 7, 20, 10, 0, 0, tzinfo=tzutc())
    assert program.channel['id'] == 4
    assert program.work.id == 4681
    assert program.episode.id == 75187


class TestRepr:
    def test_user(self):
        from annict.models import User
        json = {
            "id": 2,
            "username": "shimbaco",
            "name": "Koji Shimba",
            "description": "",
            "url": None,
            "records_count": 1234,
            "created_at": "2016-05-03T19:06:59.929Z"
        }
        user = User.parse(None, json)
        assert user.__repr__() == '<User:2:Koji Shimba:@shimbaco>'

    def test_work(self):
        json = {
            'episodes_count': 21,
            'id': 4636,
            'media': 'tv',
            'media_text': 'TV',
            'official_site_url': 'http://re-zero-anime.jp/',
            'released_on': '2016-04-03',
            'released_on_about': '',
            'season_name': '2016-spring',
            'season_name_text': '2016年春',
            'title': 'Re:ゼロから始める異世界生活',
            'title_kana': 'りぜろからはじめるいせかいせいかつ',
            'twitter_hashtag': 'rezero',
            'twitter_username': 'Rezero_official',
            'watchers_count': 970,
            'wikipedia_url': ('https://ja.wikipedia.org/wiki/Re:%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E5'
                              '%A7%8B%E3%82%81%E3%82%8B%E7%95%B0%E4%B8%96%E7%95%8C%E7%94%9F%E6%B4%BB'),
        }
        from annict.models import Work

        work = Work.parse('dummy_api', json)
        assert work.__repr__() == '<Work:4636:Re:ゼロから始める異世界生活>'

    def test_episode(self):
        json = {
            "id": 45,
            "number": None,
            "number_text": "第2話",
            "sort_number": 2,
            "title": "殺戮の夢幻迷宮",
            "records_count": 0,
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
                "number": None,
                "number_text": "第1話",
                "sort_number": 1,
                "title": " 夢の騎士達",
                "records_count": 0
            },
            "next_episode": None
        }
        from annict.models import Episode

        episode = Episode.parse(None, json)
        assert episode.__repr__() == '<Episode:45:第2話:殺戮の夢幻迷宮:NEWドリームハンター麗夢>'

    def test_record(self):
        json = {
            "id": 425551,
            "comment": "ゆるふわ田舎アニメかと思ったらギャグと下ネタが多めのコメディアニメだった。これはこれで。日岡さんの声良いなあ。",
            "rating": 4,
            "is_modified": False,
            "likes_count": 0,
            "comments_count": 0,
            "created_at": "2016-04-11T14:19:13.974Z",
            "user": {
                "id": 2,
                "username": "shimbaco",
                "name": "Koji Shimba",
                "description": "アニメ好きが高じてこのサービスを作りました。聖地巡礼を年に数回しています。",
                "url": "http://shimba.co",
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
                "records_count": 183
            }
        }

        from annict.models import Record

        record = Record.parse(None, json)
        assert record.__repr__() == '<Record:425551>'

    def test_program(self):
        json = {
            "id": 35387,
            "started_at": "2016-05-07T20:10:00.000Z",
            "is_rebroadcast": False,
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
                "records_count": 0
            }
        }

        from annict.models import Program

        program = Program.parse(None, json)
        assert program.__repr__() == '<Program:35387>'

    def test_activity_for_create_status_action(self):
        json = {
           "action": "create_status",
           "created_at": "2017-03-12T12:48:07.408Z",
           "id": 1535967,
           "status": {
               "kind": "watching"
           },
           "user": {
               "avatar_url": "https://api-assets.annict.com/paperclip/profiles/1160/tombo_avatars/master/d607b56162ae63bf33c460c9c88330a08303a206.jpg",
               "background_image_url": "https://api-assets.annict.com/paperclip/profiles/1160/tombo_background_images/master/6a563f8dfb602790a92e7acd78b83cfa025bd73e.jpg",
               "created_at": "2015-10-16T17:16:42.743Z",
               "description": "絵を描きます /佐世保鎮守府/ 猫飼い / 普段はwebプログラマーやってます #python #django / Pixiv: http://www.pixiv.net/member.php?id=139100 見てるアニメ: https://annict.com/@kk6",
               "id": 1229,
               "name": "あしやひろ",
               "records_count": 1470,
               "url": "https://twitter.com/kk6",
               "username": "kk6"
           },
           "work": {
               "episodes_count": 11,
               "id": 4998,
               "media": "tv",
               "media_text": "TV",
               "official_site_url": "http://gabdro.com/",
               "released_on": "",
               "released_on_about": "",
               "season_name": "2017-winter",
               "season_name_text": "2017年冬",
               "title": "ガヴリールドロップアウト",
               "title_kana": "がゔりーるどろっぷあうと",
               "twitter_hashtag": "gabdro",
               "twitter_username": "gabdroanime",
               "watchers_count": 444,
               "wikipedia_url": "https://ja.wikipedia.org/wiki/%E3%82%AC%E3%83%B4%E3%83%AA%E3%83%BC%E3%83%AB%E3%83%89%E3%83%AD%E3%83%83%E3%83%97%E3%82%A2%E3%82%A6%E3%83%88"
           }
        }

        from annict.models import Activity

        activity = Activity.parse(None, json)
        assert activity.__repr__() == '<Activity:create_status:@kk6>'
        assert activity.status == {'kind': 'watching'}
