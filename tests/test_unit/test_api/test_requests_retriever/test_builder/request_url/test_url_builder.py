from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.api.requests_retriever.builder.url.url_builder import AuthURL, SessionURL, URLBuilder, \
    URL
from gamebench_api_client.global_settings import GAMEBENCH_CONFIG
from tests import *


class StubURLBuilder(URLBuilder):
    """ Setting up the URL Builder for tests."""

    def __init__(self):
        """ Set up the init for tests."""

        super().__init__()

    def set_suffix(self):
        """ Set up the set_suffix abstract method for tests."""

        super().set_suffix()

    def set_url(self):
        """ Set up the set_url abstract method for tests."""

        super().set_url()


class TestURLBuilder(TestCase):
    """ Class to test the URL Builder base class."""

    def setUp(self):
        self.default_url_builder = StubURLBuilder()

    def test_set_suffix(self):
        """ Test the set_suffix method is in the abstract URL Builder."""

        self.assertIsNone(self.default_url_builder.set_suffix())

    def test_build_url(self):
        """ Test the set_url method is in the abstract URL Builder."""

        self.assertIsNone(self.default_url_builder.set_url())


class TestAuthURL(TestCase):
    """ Class responsible for testing the Auth URL class."""

    def setUp(self):
        self.auth_url = AuthURL()

    def test_set_suffix(self):
        """ Verify the suffix property is correctly set."""

        self.auth_url.set_suffix()
        actual = self.auth_url.suffix
        expected = AUTH_SUFFIX

        self.assertEqual(
            actual,
            expected
        )

    def test_build_url(self):
        """ Verify that the entire URL is created as expected."""

        self.auth_url.base_url = BASE_URL
        self.auth_url.version = VERSION
        self.auth_url.suffix = AUTH_SUFFIX
        self.auth_url.set_url()

        actual = self.auth_url.url
        expected = AUTH_URL

        self.assertEqual(
            actual,
            expected
        )


class TestSessionURL(TestCase):
    builder_directory = 'gamebench_api_client.api.requests_retriever.builder.url.url_builder'

    def setUp(self):
        self.session = SessionURL()

    @patch(builder_directory + '.SessionURL._set_metric')
    @patch(builder_directory + '.SessionURL._set_session_id')
    def test_set_suffix(self, mock_set_session_id, mock_set_metric):
        """ Verify the suffix is set and calls the required methods."""

        mock_set_session_id.return_value = SESSION_ID
        mock_set_metric.return_value = METRIC
        test_parameters = {
            "session_id": SESSION_ID,
            "metric": METRIC
        }
        self.session.set_suffix(**test_parameters)
        actual = self.session.suffix
        expected = SESSION_SUFFIX

        with self.subTest():
            mock_set_session_id.assert_called_once_with(SESSION_ID)
            mock_set_metric.assert_called_once_with(METRIC)
        self.assertEqual(actual, expected)

    @patch(builder_directory + '.SessionURL._build_url')
    def test_set_url(self, mock_build_url):
        """ Verify set_url correctly assigns the url variable."""

        mock_build_url.return_value = DEFAULT_SESSION_URL
        self.session.set_url()
        actual = self.session.url

        with self.subTest():
            mock_build_url.assert_called_once_with()
        self.assertEqual(actual, DEFAULT_SESSION_URL)

    def test_build_url(self):
        """ Verify the build_url correctly creates the URL."""

        self.session.base_url = BASE_URL
        self.session.version = VERSION
        self.session.suffix = SESSION_SUFFIX
        self.session.session_id = '/' + SESSION_ID
        self.session.metric = METRIC
        actual = self.session._build_url()

        self.assertEqual(actual, DEFAULT_SESSION_URL)

    def test_set_session_id(self):
        """ Verify the session id is set."""

        self.session._set_session_id(SESSION_ID)
        actual = self.session.session_id
        expected = '/' + SESSION_ID
        self.assertEqual(actual, expected)

    def test_set_session_id_with_empty_session(self):
        """ Session ID is blank."""

        self.session._set_session_id('')
        actual = self.session.session_id
        expected = ''
        self.assertEqual(actual, expected)

    def test_set_metric(self):
        """ Verify the metric is set."""

        self.session._set_metric(METRIC)
        actual = self.session.metric
        self.assertEqual(actual, METRIC)


class TestURL(TestCase):

    def setUp(self):
        self.url = URL()

    def test_base_url_attribute(self):
        """ The URL.base_url attribute should match the URL set in the global settings."""

        actual = self.url.base_url
        expected = GAMEBENCH_CONFIG['url']
        self.assertEqual(actual, expected)

    def test_version_attribute(self):
        """ The URL.version attribute should match the URL set in the global settings."""

        actual = self.url.version
        expected = GAMEBENCH_CONFIG['api_version']
        self.assertEqual(actual, expected)
