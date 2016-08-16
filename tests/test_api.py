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
