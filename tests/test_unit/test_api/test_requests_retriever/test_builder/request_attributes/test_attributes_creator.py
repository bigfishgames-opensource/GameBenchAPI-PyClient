""" Unit tests for the Attribute module."""

from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.api.requests_retriever.builder.attributes.attributes_creator import \
    Attributes
from tests import AUTH_HEADERS, AUTH_TOKEN, DEFAULT_SESSION_HEADERS, METRIC, \
    NO_METRIC_HEADERS


class TestAttributes(TestCase):
    """ Unit tests for the Attributes class."""

    def setUp(self):
        self.attributes = Attributes()

    def test_get_headers_includes_empty_metric(self):
        """ Verify the correct headers are returned if the metric key is empty."""

        test_parameters = {
            "metric": "",
            "auth_token": AUTH_TOKEN
        }

        actual = self.attributes.get_headers(**test_parameters)
        expected = NO_METRIC_HEADERS

        self.assertEqual(
                actual,
                expected
        )

    def test_get_headers_includes_metric(self):
        """ Verify the correct headers are returned if a metric key is present."""

        test_parameters = {
            "metric": METRIC,
            "auth_token": AUTH_TOKEN
        }

        actual = self.attributes.get_headers(**test_parameters)
        expected = DEFAULT_SESSION_HEADERS

        self.assertEqual(
                actual,
                expected
        )

    def test_get_headers_for_auth(self):
        """ Verify correct headers are returned for an authentication call.

            If there is no 'metric' key in the parameters it is set as an auth call.
        """

        test_parameters = {}

        actual = self.attributes.get_headers(**test_parameters)
        expected = AUTH_HEADERS

        self.assertEqual(
                actual,
                expected
        )

    def test_get_params(self):
        """ Verify the correct parameters are returned.

            The test parameter used is an example of a query that could
            be used for calls to the GameBench API.  When added to the URL
            it would return the last 15 entries that matched the search.
        """

        test_parameters = {
            "params": "pageSize=15"
        }

        actual = self.attributes.get_params(**test_parameters)
        expected = "pageSize=15"

        self.assertEqual(
                actual,
                expected
        )

    @patch(
            'gamebench_api_client.api.requests_retriever.builder.attributes.attributes_creator.Attributes'
            '._is_auth_request')
    def test_get_data_with_username(self, mock_is_auth_request):
        """ Verify the correct data is returned if a username and password are present.

            If there is a username key that means it is an auth request so we return
            the username and password as the data variable in the request builder.
        """

        mock_is_auth_request.return_value = True
        test_parameters = {
            "password": "test_password",
            "username": "test_user_name"
        }

        actual = self.attributes.get_data(**test_parameters)
        expected = {
            "username": "test_user_name",
            "password": "test_password"
        }

        with self.subTest():
            mock_is_auth_request.assert_called_once_with(**test_parameters)

        self.assertEqual(
                actual,
                expected
        )

    @patch(
            'gamebench_api_client.api.requests_retriever.builder.attributes.attributes_creator.Attributes'
            '._is_auth_request')
    def test_get_data_without_username(self, mock_is_auth_request):
        """ Verify the correct data is returned if there is no username key."""

        mock_is_auth_request.return_value = False
        test_parameters = {
            "data": "test_data",
        }

        actual = self.attributes.get_data(**test_parameters)
        expected = "test_data"

        self.assertEqual(
                actual,
                expected
        )

    def test_is_auth_request(self):
        """ Verify True is returned if parameters include 'username' key."""

        test_parameters = {
            "username": "test_user_name",
            "password": "test_password"
        }

        actual = self.attributes._is_auth_request(**test_parameters)

        self.assertTrue(actual)

    def test_get_session_headers(self):
        """ Verify _get_session_headers returns the expected headers."""

        error_message = "\nTest: {} \nExpected: {}\nActual:   {}\n"
        test_params = {
            "no_metric": {
                "metric": "",
                "headers": NO_METRIC_HEADERS
            },
            "metric_present": {
                "metric": METRIC,
                "headers": DEFAULT_SESSION_HEADERS
            }
        }

        for test, params in test_params.items():
            request_parameters = {
                'metric': params['metric'],
                'auth_token': AUTH_TOKEN,
                'headers': params['headers']
            }

            expected = params["headers"]
            actual = self.attributes._get_session_headers(**request_parameters)

            self.assertEqual(
                    expected,
                    actual,
                    error_message.format(
                            test,
                            expected,
                            actual
                    )
            )
