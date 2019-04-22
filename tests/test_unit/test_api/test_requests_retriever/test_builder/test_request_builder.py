""" Unit tests for the Request Builder module."""

from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.api.requests_retriever.builder.request_builder import AuthRequest, Request, RequestBuilder, \
    SessionRequest
from gamebench_api_client.api.requests_retriever.builder.url.url_director import URLDirector
from tests import *

patch_method = 'Method'
patch_attributes = 'Attributes'
patch_request = 'Request'


class DefaultRequestBuilder(RequestBuilder):
    """ Sets up the Request Builder in order to test it."""

    def __init__(self, **request_parameters):
        """ Setup the init for tests.
        :param **request_parameters:
        """

        super().__init__(**request_parameters)

    def set_method(self):
        """ Setup the set_method method for tests."""

        super().set_method()

    def set_url(self, url_director):
        """ Setup the set_url method for tests."""

        super().set_url(url_director)

    def set_headers(self):
        """ Setup set_headers method for tests."""

        super().set_headers()

    def set_params(self):
        """ Setup the set_params method for tests."""

        super().set_params()

    def set_data(self):
        """ Setup the get_results method for tests."""

        super().set_data()


class TestRequestBuilder(TestCase):
    """Class to verify the abstract Request Builder class is set up."""

    @patch(REQUEST_BUILDER_PATH + patch_method)
    @patch(REQUEST_BUILDER_PATH + patch_attributes)
    @patch(REQUEST_BUILDER_PATH + patch_request)
    def setUp(self, mock_request, mock_attributes, mock_method):
        mock_request.return_value = "Test"
        self.mock_request = mock_request
        mock_attributes.return_value = "Test"
        self.mock_attributes = mock_attributes
        mock_method.return_value = "Test"
        self.mock_method = mock_method
        self.builder = DefaultRequestBuilder()

    def test_init_creates_request(self):
        """ Verify the init creates a Request object."""

        with self.subTest():
            self.mock_request.assert_called_once_with()
        with self.subTest():
            self.mock_attributes.assert_called_once_with()
        with self.subTest():
            self.mock_method.assert_called_once_with()

    def test_set_method(self):
        """ Verify the method attribute is created in the Request object."""

        self.assertEqual(self.builder.set_method(), None)

    def test_set_url(self):
        """ Verify the url attribute is created in the Request object."""

        self.assertEqual(self.builder.set_url("Test"), None)

    def test_set_headers(self):
        """ Verify the headers attribute is created in the Request object."""

        self.assertEqual(self.builder.set_headers(), None)

    def test_set_params(self):
        """ Verify the params attribute is created in the Request object."""

        self.assertEqual(self.builder.set_params(), None)

    def test_set_data(self):
        """ Verify the data attribute is created in the Request object."""

        self.assertEqual(self.builder.set_data(), None)


class TestAuthRequest(TestCase):
    """ Tests for the AuthRequest concrete builder."""

    @patch(REQUEST_BUILDER_PATH + patch_method)
    @patch(REQUEST_BUILDER_PATH + patch_attributes)
    @patch(REQUEST_BUILDER_PATH + patch_request)
    def setUp(self, mock_request, mock_attributes, mock_method):
        self.mock_get_method = mock_method.return_value
        self.mock_get_method.get_method.return_value = "POST"
        self.mock_attributes = mock_attributes.return_value
        self.mock_attributes.get_headers.return_value = AUTH_HEADERS
        self.mock_attributes.get_params.return_value = "test_params"
        self.mock_attributes.get_data.return_value = AUTH_DATA
        self.auth_request = AuthRequest()

    def test_set_auth_method(self):
        """ Verify the method is set correctly for authorization."""

        self.auth_request.set_method()

        expected = 'POST'
        actual = self.auth_request.request.method

        self.assertEqual(
            expected,
            actual)

    @patch(TEST_URL_DIRECTOR_PATH)
    def test_set_auth_url(self, mock_url):
        """ Verify the correct authorization URL is created.

            This calls the URL Builder for the creation of the URL.
        """
        mock_url.return_value = AUTH_URL
        url_director = URLDirector()
        self.auth_request.set_url(url_director)

        actual = self.auth_request.request.url
        expected = AUTH_URL

        self.assertEqual(
            expected,
            actual
        )

    def test_set_auth_headers(self):
        """ Verify the correct headers are set for authorization."""

        self.auth_request.set_headers()

        actual = self.auth_request.request.headers
        expected = AUTH_HEADERS

        self.assertEqual(
            expected,
            actual
        )

    def test_no_params_set(self):
        """ Verify there are no params for authorization."""

        actual = self.auth_request.set_params()
        expected = None

        self.assertEqual(
            expected,
            actual
        )

    def test_set_data(self):
        """ Verify the data contains the username and password."""

        self.auth_request.set_data()

        actual = self.auth_request.request.data
        expected = AUTH_DATA

        self.assertEqual(
            actual,
            expected
        )


class TestSessionRequest(TestCase):
    """ Tests for the SessionRequest concrete builder."""

    @patch(REQUEST_BUILDER_PATH + patch_method)
    @patch(REQUEST_BUILDER_PATH + patch_attributes)
    @patch(REQUEST_BUILDER_PATH + patch_request)
    def setUp(self, mock_request, mock_attributes, mock_method):
        self.mock_get_method = mock_method.return_value
        self.mock_get_method.get_method.return_value = "GET"
        self.mock_attributes = mock_attributes.return_value
        self.mock_attributes.get_headers.return_value = DEFAULT_SESSION_HEADERS
        self.mock_attributes.get_params.return_value = "test_params"
        self.mock_attributes.get_data.return_value = {"test_data": "test_data"}
        self.session = SessionRequest()

    def test_set_session_method(self):
        """ Verify the method is set correctly for a session.

            This test is for session requests that contain a metric.
        """

        self.session.set_method()

        actual = self.session.request.method
        expected = "GET"

        self.assertEqual(
            expected,
            actual
        )

    @patch(TEST_URL_DIRECTOR_PATH)
    def test_set_session_url(self, mock_url):
        """ Verify the proper URL is set for session requests.

            The URLs are created in the URL Builder.
        """
        mock_session_url = mock_url.return_value
        mock_session_url.get_session_url.return_value = DEFAULT_SESSION_URL

        self.session.set_url(mock_session_url)

        actual = self.session.request.url
        expected = DEFAULT_SESSION_URL

        self.assertEqual(
            expected,
            actual
        )

    def test_set_session_headers(self):
        """ Verify the correct headers are set for session requests."""

        self.session.set_headers()

        actual = self.session.request.headers
        expected = DEFAULT_SESSION_HEADERS

        self.assertEqual(
            expected,
            actual
        )

    def test_set_session_params(self):
        """Verify the correct params are set for session requests."""

        self.session.set_params()

        expected = "test_params"
        actual = self.session.request.params

        self.assertEqual(
            expected,
            actual
        )

    def test_set_session_data(self):
        """ Verify the correct data is set for session requests."""

        self.session.set_data()

        actual = self.session.request.data
        expected = {
            "test_data": "test_data"
        }

        self.assertEqual(
            expected,
            actual
        )


class TestRequest(TestCase):
    """ Tests for the Request class."""

    def test_can_call_request_object(self):
        """ Verify a Request object is created."""

        self.assertTrue(
            Request(),
            None
        )
