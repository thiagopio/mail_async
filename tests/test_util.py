# -*- coding: utf-8 -*-
from model.util import Util
import datetime
import pytest


def test_text2date_iso():
    now = datetime.datetime.now()
    # ISO 8601
    date = Util.text2date(now.isoformat(), Util.ISO_FORMAT)
    assert now == date


def test_text2date_utc():
    example_date = '2016-06-09T15:42:00-03:00'
    date = Util.text2date(example_date, Util.UTC_FORMAT)
    assert date.isoformat() == '2016-06-09T15:42:00'


def test_text2date_invalid():
    with pytest.raises(ValueError):
        Util.text2date('2016-06-09T15:42:00', Util.UTC_FORMAT)


def test_text2date_none():
    with pytest.raises(TypeError):
        Util.text2date(None, Util.UTC_FORMAT)