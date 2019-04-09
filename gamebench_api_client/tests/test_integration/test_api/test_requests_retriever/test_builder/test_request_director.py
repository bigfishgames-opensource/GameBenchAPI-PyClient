""" Integration tests for the Request Director module."""

from unittest import TestCase

from gamebench_api_client.api.requests_retriever.builder.request_director import RequestDirector
from gamebench_api_client.tests.fixtures.constants import AUTH_DATA, AUTH_HEADERS, AUTH_TOKEN, AUTH_URL, BASE_URL, \
    METRIC_TEST_PARAMS, PASSWORD, SESSION_SUFFIX, USERNAME, VERSION


class TestRequestDirector(TestCase):
    """ Tests for the Request Director class."""

    def setUp(self):
        self.director = RequestDirector()

    def test_init(self):
        """ Verify the init creates an empty _builder variable."""

        self.assertEqual(self.director._builder, None)


class TestGetAuthRequest(TestCase):
    """ Tests for the GetAuth Request class."""

    def setUp(self):
        self.director = RequestDirector()

    def test_get_auth_request(self):
        """ Test to check that get_auth_request returns expected dict."""
        data = AUTH_DATA

        expected = {
            "method": "POST",
            "url": AUTH_URL,
            "attributes": {
                "headers": AUTH_HEADERS,
                "auth": (USERNAME, PASSWORD)
            }
        }
        actual = self.director.get_auth_request(**data)

        self.assertEqual(
                expected,
                actual
        )

    def test_get_session_request(self):
        """ Test to check that get_session_request returns expected dict."""

        error_message = "\nTest: {} \nExpected: {}\nActual:   {}\n"
        test_params = METRIC_TEST_PARAMS

        for test, params in test_params.items():
            request_parameters = {
                'method': params['method'],
                'session_id': params["session_id"],
                'metric': params["metric"],
                'auth_token': AUTH_TOKEN,
                "params": "test_params",
                "data": {
                    "test_data": "test_data"
                }
            }
            expected = {
                "method": params["method"],
                "url": BASE_URL + VERSION + SESSION_SUFFIX + params["session_id"] + params["metric"],
                "attributes": {
                    "headers": params["headers"],
                    "params": "test_params",
                    "data": {
                        "test_data": "test_data"
                    }
                }
            }
            actual = self.director.get_session_request(**request_parameters)

            self.assertEqual(
                    expected,
                    actual,
                    error_message.format(
                            test,
                            expected,
                            actual
                    )
            )
