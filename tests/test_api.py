# -*- coding: utf-8 -*-


def test_api():
    from annict.api import API
    from annict.services import (
        WorksService,
        EpisodesService,
        RecordsService,
        MeService,
        MeProgramsService,
        MeStatusesService,
        MeRecordsService,
        MeWorksService,
    )

    api = API('token')

    assert isinstance(api.works, WorksService)
    assert isinstance(api.episodes, EpisodesService)
    assert isinstance(api.records, RecordsService)
    assert isinstance(api.me, MeService)
    assert isinstance(api.me.programs, MeProgramsService)
    assert isinstance(api.me.statuses, MeStatusesService)
    assert isinstance(api.me.records, MeRecordsService)
    assert isinstance(api.me.works, MeWorksService)


def test_me_statuses_create(monkeypatch):
    from annict.client import Client
    def mockreturn(self, path, params):
        return True
    monkeypatch.setattr(Client, 'post', mockreturn)

    from annict.api import API
    api = API('token')
    r = api.me.statuses.create(work_id=1, kind='wanna_watch')
    assert r == True

