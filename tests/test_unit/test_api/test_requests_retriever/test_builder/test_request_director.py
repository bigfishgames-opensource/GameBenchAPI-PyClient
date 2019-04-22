""" Unit tests for the request director."""

from unittest import TestCase
from unittest.mock import Mock, patch

from gamebench_api_client.api.requests_retriever.builder.request_director import DirectorLoader, RequestDirector
from tests import *


class TestRequestDirector(TestCase):
    """ Tests for the Request Director module."""

    def setUp(self):
        self.director = RequestDirector()

    def test_init_creates_builder_object(self):
        """ Verify the init simply creates a _builder variable."""

        self.assertEqual(self.director._builder, None)

    def test_auth_to_dict(self):
        """ Verify the helper method correctly turns the object into a dictionary."""

        mock = Mock()
        mock.request.method = 'POST'
        mock.request.url = AUTH_URL
        mock.request.headers = AUTH_HEADERS
        mock.request.data = AUTH_DATA

        actual = self.director._auth_to_dict(mock)
        expected = {
            'method': mock.request.method,
            'url': mock.request.url,
            'attributes': {
                'headers': mock.request.headers,
                'auth': (
                    mock.request.data['username'],
                    mock.request.data['password']
                )
            }
        }

        self.assertEqual(
            actual,
            expected
        )

    def test_session_to_dict(self):
        """ Verify the helper method correctly turns the object into a dictionary."""

        mock = Mock()
        mock.request.method = 'GET'
        mock.request.url = DEFAULT_SESSION_URL
        mock.request.headers = DEFAULT_SESSION_HEADERS
        mock.request.params = "test_params"
        mock.request.data = SESSION_DATA

        actual = self.director._session_to_dict(mock)
        expected = {
            'method': mock.request.method,
            'url': mock.request.url,
            'attributes': {
                'headers': mock.request.headers,
                'params': mock.request.params,
                'data': mock.request.data
            }
        }

        self.assertEqual(
            actual,
            expected
        )


class TestDirectorLoader(TestCase):

    @patch('gamebench_api_client.api.requests_retriever.builder.request_director.URLDirector')
    def test_set_url_director(self, mock_director):
        loader = DirectorLoader()
        loader.set_url_director()
        mock_director.assert_called()
