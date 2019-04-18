import json
from unittest import TestCase
from unittest.mock import patch

import pandas
import requests_mock
from pandas.io.json import json_normalize
from pandas.testing import assert_frame_equal

from gamebench_api_client.api.requests_retriever.request_adapter.adapter import RequestsAdapter
from gamebench_api_client.api.response.response_mediator import GenericMediator, SessionDetailMediator, \
    TimeSeriesMediator, AuthenticationMediator
from gamebench_api_client.api.response.response_retriever import ResponseRetriever
from tests import *


class TestTimeSeriesMediator(TestCase):
    """ Tests for the TimeSeriesMediator."""

    def setUp(self):
        self.error_message = "\nTest: {} \nExpected: {}\nActual:   {}\n"
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "cpu_multiple_sessions.json")) as \
                json_data:
            self.time_series_json = json.load(json_data)

    @requests_mock.Mocker()
    def test_set_data(self, mock_return):
        """ Verify get_results returns a DataFrame."""

        adapter = RequestsAdapter(**DEFAULT_EXPECTED_REQUEST_PARAMS)
        mock_return.request(
            "GET",
            DEFAULT_SESSION_URL,
            json=self.time_series_json["response"]
        )

        expected = json_normalize(
            adapter.request().json(),
            'samples',
            ['id', 'sessionId']
        )
        self.mediator = TimeSeriesMediator(**DEFAULT_REQUEST_PARAMS)
        actual = self.mediator.get_results()

        assert_frame_equal(
            expected,
            actual
        )


class TestSessionDetailMediator(TestCase):
    """ Tests for the SessionDetailMediator."""

    def setUp(self):
        self.error_message = "\nTest: {} \nExpected: {}\nActual:   {}\n"
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "sessionid.json")) as json_data:
            self.session_app_json = json.load(json_data)

    @requests_mock.Mocker()
    def test_set_data(self, mock_return):
        """ Verify get_results returns a DataFrame."""

        mock_return.request(
            "GET",
            "https://api.production.gamebench.net/v1/sessions/session_id",
            json=self.session_app_json["response"]
        )

        expected = pandas.DataFrame(data=[self.session_app_json['response']['app']])
        self.mediator = SessionDetailMediator(**DEFAULT_SESSION_DETAIL_PARAMS)
        actual = self.mediator.get_results()

        assert_frame_equal(
            expected,
            actual
        )


class TestGenericFrameMediator(TestCase):
    """ Tests for the GenericMediator."""

    def setUp(self):
        self.error_message = "\nTest: {} \nExpected: {}\nActual:   {}\n"
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "sessionid.json")) as json_data:
            self.generic_frame_json = json.load(json_data)

    @requests_mock.Mocker()
    def test_set_data(self, mock_return):
        """ Verify get_results returns a DataFrame."""

        adapter = RequestsAdapter(**DEFAULT_EXPECTED_REQUEST_PARAMS)
        mock_return.request(
            "GET",
            DEFAULT_SESSION_URL,
            json=self.generic_frame_json["response"]
        )

        expected = pandas.DataFrame([adapter.request().json()])
        self.mediator = GenericMediator(**DEFAULT_REQUEST_PARAMS)
        actual = self.mediator.get_results()

        assert_frame_equal(
            expected,
            actual
        )


class TestResponseRetriever(TestCase):
    """ Tests for the ResponseMediator."""

    def setUp(self):
        self.error_message = "\nTest: {} \nExpected: {}\nActual:   {}\n"
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "cpu_multiple_sessions.json")) as \
                json_data:
            self.time_series_json = json.load(json_data)
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "sessionid.json")) as json_data:
            self.session_id_json = json.load(json_data)
        self.test_params = {
            "metric": {
                'method': 'GET',
                'metric': '/cpu',
                "params": 'test_params',
                'session_id': SESSION_ID,
                "url": DEFAULT_SESSION_URL,
                "data": {'test_data': 'test_data'},
                "headers": DEFAULT_SESSION_HEADERS,
                "attributes": {
                    'params': 'test_params',
                    'headers': DEFAULT_SESSION_HEADERS,
                    'data': {'test_data': 'test_data'}
                }
            },
            "no_metric": {
                'method': 'POST',
                'metric': '',
                "params": 'test_params',
                'session_id': '',
                'url': "https://api.production.gamebench.net/v1/sessions",
                "data": {'test_data': 'test_data'},
                "headers": NO_METRIC_HEADERS,
                "attributes": {
                    'params': 'test_params',
                    'headers': NO_METRIC_HEADERS,
                    'data': {'test_data': 'test_data'}
                }
            },
            "session": {
                'method': 'GET',
                'metric': '',
                "params": 'test_params',
                'session_id': SESSION_ID,
                'url': "https://api.production.gamebench.net/v1/sessions/session_id",
                "data": {'test_data': 'test_data'},
                "headers": DEFAULT_SESSION_HEADERS,
                "attributes": {
                    'params': 'test_params',
                    'headers': DEFAULT_SESSION_HEADERS,
                    'data': {'test_data': 'test_data'}
                }
            }
        }

    @patch('gamebench_api_client.api.response.response_retriever.RequestsAdapter')
    def test_get_response_json_gets_expected_request_dict(self, mock_return):
        """ Verify get_response_json.request is set to the correct dict."""

        # We don't want to make an actual request and requests_mock is quite slow, so we don't want to use it
        # unnecessarily. Since this isn't actually used as part of the test, I'm just returning an empty string.
        mock_return.request.return_value = ""

        for test, params in self.test_params.items():
            session_parameters = {
                'method': params['method'],
                'session_id': params['session_id'],
                'metric': params['metric'],
                'auth_token': AUTH_TOKEN,
                "params": params['params'],
                "data": params['data']
            }
            self.retriever = ResponseRetriever(**session_parameters)
            self.retriever.get_response_json()

            expected = {
                "method": params['method'],
                "url": params['url'],
                "attributes": params['attributes']
            }
            actual = self.retriever.request

            self.assertEqual(
                expected,
                actual,
                self.error_message.format(
                    test,
                    expected,
                    actual
                )
            )

    @requests_mock.Mocker()
    def test_get_response_json_creates_expected_json_with_time_series_data(self, mock_return):
        """ Verify the json we are expecting is returned from the Adapter."""

        for test, params in self.test_params.items():
            session_parameters = {
                'method': params['method'],
                'session_id': params['session_id'],
                'metric': params['metric'],
                'auth_token': AUTH_TOKEN,
                "params": params['params'],
                "data": params['data']
            }
            expected_request_parameters = {
                "method": params['method'],
                "url": params['url'],
                "attributes": params['attributes']
            }

            adapter = RequestsAdapter(**expected_request_parameters)
            mock_return.request(
                params['method'],
                params['url'],
                json=self.time_series_json["response"]
            )

            expected_json = adapter.request().json()
            expected = expected_json['samples']

            self.retriever = ResponseRetriever(**session_parameters)
            actual_json = self.retriever.get_response_json()
            actual = actual_json['samples']

            self.assertEqual(
                expected,
                actual,
                self.error_message.format(
                    test,
                    expected,
                    actual
                )
            )


class TestAuthenticationMediator(TestCase):
    """ Tests for the AuthenticationMediator."""

    def setUp(self):
        self.error_message = "\nTest: {} \nExpected: {}\nActual:   {}\n"
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "auth_sample.json")) as json_data:
            self.auth_json = json.load(json_data)

    @requests_mock.Mocker()
    def test_set_data(self, mock_return):
        """ Verify get_results returns an auth token."""

        adapter = RequestsAdapter(**AUTH_ATTRIBUTES)
        mock_return.request(
            "POST",
            AUTH_URL,
            json=self.auth_json["response"]
        )
        expected = adapter.request().json()
        self.mediator = AuthenticationMediator(**AUTH_DATA)
        actual = self.mediator.get_results()

        self.assertEqual(actual, expected)
