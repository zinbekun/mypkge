# test_talker.py
import pytest
from datetime import datetime
from mypkg.talker import cb

class DummyRequest:
    def __init__(self, time_value=None):
        self.time = time_value

class DummyResponse:
    def __init__(self):
        self.now = None
        self.time = None

def test_cb_now():
    req = DummyRequest(time_value="now")
    res = DummyResponse()
    cb(req, res)
    assert res.now is not None
    # now は文字列形式
    assert isinstance(res.now, str)

def test_cb_unknown():
    req = DummyRequest(time_value="later")
    res = DummyResponse()
    cb(req, res)
    assert res.time == "unknown"

