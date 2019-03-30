from unittest.mock import Mock

import pytest

from libpythonpro_barthjr import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/19367707?v=4'
    resp_mock.json.return_value = {
        'login': 'BarthJr', 'id': 19367707,
        'avatar_url': url, 'gravatar_id': '',
    }
    get_mock = mocker.patch('libpythonpro_barthjr.github_api.requests.get')
    get_mock.return_value = resp_mock
    yield url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('barthjr')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('barth')
    assert 'https://avatars2.githubusercontent.com/u/3066749?v=4' == url
