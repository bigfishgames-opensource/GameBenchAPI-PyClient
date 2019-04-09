import json
import os
from unittest import TestCase
from unittest.mock import patch

import pandas
import requests_mock
from pandas.io.json import json_normalize
from pandas.testing import assert_frame_equal

from gamebench_api_client.api.requests_retriever.request_adapter.adapter import RequestsAdapter
from gamebench_api_client.api.response.response_mediator import GenericMediator, ResponseRetriever, \
    SessionDetailMediator, TimeSeriesMediator
from gamebench_api_client.tests import PARENT_DIR
from gamebench_api_client.tests.fixtures.constants import API_SAMPLES, AUTH_TOKEN, DEFAULT_EXPECTED_REQUEST_PARAMS, \
    DEFAULT_REQUEST_PARAMS, DEFAULT_SESSION_HEADERS, DEFAULT_SESSION_URL, NO_METRIC_EXPECTED_REQUEST_PARAMS, \
    NO_METRIC_HEADERS, NO_METRIC_REQUEST_PARAMS, SESSION_ID


class TestTimeSeriesMediator(TestCase):
    """ Tests for the TimeSeriesMediator."""

    def setUp(self):
        self.mediator = TimeSeriesMediator()
        self.error_message = "\nTest: {} \nExpected: {}\nActual:   {}\n"
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "cpu_multiple_sessions.json")) as \
                json_data:
            self.time_series_json = json.load(json_data)

    @requests_mock.Mocker()
    def test_set_data(self, mock_return):
        """ Verify get_data returns a DataFrame."""

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
        actual = self.mediator.get_data(**DEFAULT_REQUEST_PARAMS)

        assert_frame_equal(
                expected,
                actual
        )


class TestSessionDetailMediator(TestCase):
    """ Tests for the SessionDetailMediator."""

    def setUp(self):
        self.mediator = SessionDetailMediator()
        self.error_message = "\nTest: {} \nExpected: {}\nActual:   {}\n"
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "sessionid.json")) as json_data:
            self.test_json = json.load(json_data)

    @requests_mock.Mocker()
    def test_set_data(self, mock_return):
        """ Verify get_data returns a DataFrame."""

        adapter = RequestsAdapter(**NO_METRIC_EXPECTED_REQUEST_PARAMS)
        mock_return.request(
                "POST",
                "https://api.production.gamebench.net/v1/sessions/session_id?test_params",
                json=self.test_json["response"]
        )
        series = pandas.Series(adapter.request().json())

        expected = pandas.DataFrame(
                series['app'],
                index=['app']
        )
        actual = self.mediator.get_data(**NO_METRIC_REQUEST_PARAMS)

        assert_frame_equal(
                expected,
                actual
        )


class TestGenericFrameMediator(TestCase):
    """ Tests for the GenericMediator."""

    def setUp(self):
        self.mediator = GenericMediator()
        self.error_message = "\nTest: {} \nExpected: {}\nActual:   {}\n"
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "sessionid.json")) as json_data:
            self.generic_frame_json = json.load(json_data)

    @requests_mock.Mocker()
    def test_set_data(self, mock_return):
        """ Verify get_data returns a DataFrame."""

        adapter = RequestsAdapter(**DEFAULT_EXPECTED_REQUEST_PARAMS)
        mock_return.request(
                "GET",
                DEFAULT_SESSION_URL,
                json=self.generic_frame_json["response"]
        )

        expected = pandas.DataFrame(adapter.request().json())
        actual = self.mediator.get_data(**DEFAULT_REQUEST_PARAMS)

        assert_frame_equal(
                expected,
                actual
        )


class TestResponseRetriever(TestCase):
    """ Tests for the TimeSeriesMediator."""

    def setUp(self):
        self.retriever = ResponseRetriever()
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
                'url': "https://api.production.gamebench.net/v1/sessions/session_id",
                "data": {'test_data': 'test_data'},
                "headers": NO_METRIC_HEADERS,
                "attributes": {
                    'params': 'test_params',
                    'headers': NO_METRIC_HEADERS,
                    'data': {'test_data': 'test_data'}
                }
            }
        }

    @patch('gamebench_api_client.api.response.response_mediator.RequestsAdapter')
    def test_get_response_json_gets_expected_request_dict(self, mock_return):
        """ Verify get_response_json.request is set to the correct dict."""

        # We don't want to make an actual request and requests_mock is quite slow, so we don't want to use it
        # unnecessarily. Since this isn't actually used as part of the test, I'm just returning an empty string.
        mock_return.request.return_value = ""

        for test, params in self.test_params.items():
            session_parameters = {
                'method': params['method'],
                'session_id': SESSION_ID,
                'metric': params['metric'],
                'auth_token': AUTH_TOKEN,
                "params": params['params'],
                "data": params['data']
            }
            self.retriever.get_response_json(**session_parameters)

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
                'session_id': SESSION_ID,
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

            actual_json = self.retriever.get_response_json(**session_parameters)
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
