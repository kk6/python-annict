# -*- coding: utf-8 -*-
import responses


@responses.activate
def test_status_code_200():
    from annict.client import Client
    responses.add(responses.GET, 'https://api.annict.com/v1/works',
                  body='{"title": "ゼロから始める異世界生活"}', status=200,
                  content_type='application/json')

    client = Client('tokenxxx')
    resp = client.request('GET', 'works', {})

    assert responses.calls[0].response.status_code == 200
    assert resp == {"title": "ゼロから始める異世界生活"}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'https://api.annict.com/v1/works?access_token=tokenxxx'


@responses.activate
def test_status_code_204():
    from annict.client import Client
    responses.add(responses.POST, 'https://api.annict.com/v1/me/statuses',
                  body='', status=204)

    client = Client('tokenxxx')
    resp = client.request('POST', 'me/statuses', dict(work_id=1, kind='wanna_watch'))

    assert responses.calls[0].response.status_code == 204
    assert resp is True
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'https://api.annict.com/v1/me/statuses?access_token=tokenxxx&work_id=1&kind=wanna_watch'
    )

