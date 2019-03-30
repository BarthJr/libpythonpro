from unittest.mock import Mock

from libpythonpro_barthjr import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'BarthJr', 'id': 19367707,
        'avatar_url': 'https://avatars0.githubusercontent.com/u/19367707?v=4', 'gravatar_id': '',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('barthjr')
    assert 'https://avatars0.githubusercontent.com/u/19367707?v=4' == url
