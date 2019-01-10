# -*- coding: utf-8 -*-
import pytest
import responses


@responses.activate
def test_cursor_supported(api_factory):
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
    responses.add(
        responses.GET,
        "https://api.annict.com/v1/works",
        body=json,
        status=200,
        content_type="application/json",
    )
    api = api_factory.create()
    from annict.cursors import SimpleCursor

    gen = SimpleCursor(api.works).cursor()
    result = next(gen)
    assert result.title == "SHIROBAKO"
    with pytest.raises(StopIteration):
        next(gen)


@responses.activate
def test_cursor_unsupported(api_factory):
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
    responses.add(
        responses.GET,
        "https://api.annict.com/v1/me",
        body=json,
        status=200,
        content_type="application/json",
    )
    api = api_factory.create()
    from annict.cursors import SimpleCursor

    with pytest.raises(TypeError):
        SimpleCursor(api.me).cursor()
