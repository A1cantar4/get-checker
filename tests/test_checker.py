import pytest
import requests
from get_checker.checker import check_website


def test_online_site(monkeypatch):
    """Simulate the status 200."""
    class MockResponse:
        status_code = 200

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    assert check_website("http://fakeurl.com") is True


def test_offline_site(monkeypatch):
    """Simulate error of conection."""
    def mock_get(*args, **kwargs):
        raise requests.ConnectionError()

    monkeypatch.setattr(requests, "get", mock_get)
    assert check_website("http://fakeurl.com") is False


def test_timeout_site(monkeypatch):
    """Simulate timeout."""
    def mock_get(*args, **kwargs):
        raise requests.Timeout()

    monkeypatch.setattr(requests, "get", mock_get)
    assert check_website("http://fakeurl.com") is False