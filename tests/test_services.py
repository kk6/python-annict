# -*- coding: utf-8 -*-


class DummyClient(object):

    def get(self, path, params):
        return path, params

    def post(self, path, params):
        return path, params

    def patch(self, path, params):
        return path, params

    def delete(self, path):
        return path


def test_works_get():
    from annict.services import WorksService
    works = WorksService(DummyClient())
    title = "ゼロから始める異世界生活"
    ret = works.get(filter_title=title)
    assert ret[0] == 'works' and ret[1] == {'filter_title': title}


def test_episodes_get():
    from annict.services import EpisodesService
    works = EpisodesService(DummyClient())
    work_ids = [1234, 98765]
    ret = works.get(filter_work_ids=work_ids)
    assert ret[0] == 'episodes' and ret[1] == {'filter_work_ids': '1234,98765'}
