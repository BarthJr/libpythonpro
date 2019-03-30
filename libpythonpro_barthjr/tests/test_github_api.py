from unittest.mock import Mock

import pytest

from libpythonpro_barthjr import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('barthjr')
    assert avatar_url == url


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/19367707?v=4'
    resp_mock.json.return_value = {
        'login': 'BarthJr', 'id': 19367707,
        'avatar_url': url, 'gravatar_id': '',
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('barthjr')
    assert 'https://avatars0.githubusercontent.com/u/19367707?v=4' == url
