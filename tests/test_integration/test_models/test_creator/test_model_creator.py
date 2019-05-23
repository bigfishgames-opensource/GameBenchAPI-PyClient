import json
from unittest import TestCase

import pandas
import requests_mock
from pandas.io.json import json_normalize
from pandas.util.testing import assert_frame_equal

from gamebench_api_client.models.creator.model_creator import ModelCreator
from tests import *


class TestModelCreator(TestCase):
    """ Tests for the ModelCreator class."""

    @requests_mock.Mocker()
    def test_time_series_model_creation(self, mock_return):
        """ The ModelCreator returns the proper DataFrame."""

        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "cpu_multiple_sessions.json")) as \
                json_data:
            self.time_series_json = json.load(json_data)
        with open(os.path.join(
                PARENT_DIR + '/fixtures/' + "authentication_token.json")) as \
                json_data:
            self.auth_token = json.load(json_data)
        mock_return.request(
            'POST',
            AUTH_URL,
            json=self.auth_token
        )
        mock_return.request(
            'GET',
            DEFAULT_SESSION_URL,
            json=self.time_series_json['response']
        )
        creator = ModelCreator('Cpu', **DEFAULT_REQUEST_PARAMS)
        model = creator.get_model()
        expected = json_normalize(
            self.time_series_json['response'],
            'samples',
            ['id', 'sessionId']
        )
        actual = model.data
        assert_frame_equal(actual, expected)

    @requests_mock.Mocker()
    def test_generic_model_creation(self, mock_return):
        """ The ModelCreator returns the proper DataFrame."""

        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "notes.json")) as \
                json_data:
            self.generic_json = json.load(json_data)
        with open(os.path.join(
                PARENT_DIR + '/fixtures/' + "authentication_token.json")) as \
                json_data:
            self.auth_token = json.load(json_data)
        mock_return.request(
            'POST',
            AUTH_URL,
            json=self.auth_token
        )
        mock_return.request(
            'GET',
            GENERIC_SESSION_URL,
            json=self.generic_json['response']
        )
        creator = ModelCreator('SessionNotes', **DEFAULT_GENERIC_PARAMS)
        model = creator.get_model()
        expected = pandas.DataFrame(
            [self.generic_json['response']]
        )
        actual = model.data

        assert_frame_equal(actual, expected)

    @requests_mock.Mocker()
    def test_session_summary_details(self, mock_return):
        """ SessionSummary attributes should return the proper DataFrames."""

        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "sessionid.json")) as \
                json_data:
            self.session_app_json = json.load(json_data)
        with open(os.path.join(
                PARENT_DIR + '/fixtures/' + "authentication_token.json")) as \
                json_data:
            self.auth_token = json.load(json_data)
        mock_return.request(
            'POST',
            AUTH_URL,
            json=self.auth_token
        )
        mock_return.request(
            'GET',
            BASE_SESSION_URL,
            json=self.session_app_json['response']
        )
        creator = ModelCreator('SessionSummary', **DEFAULT_SESSION_DETAIL_PARAMS)
        model = creator.get_model()
        df = pandas.DataFrame([self.session_app_json['response']])
        expected = df.filter(['app'])
        actual = model.app

        assert_frame_equal(actual, expected)

    @requests_mock.Mocker()
    def test_keyword_search(self, mock_return):
        """ Keyword search should return the proper DataFrames.

            Regression test for https://github.com/bigfishgames/gamebenchapi-pyclient/issues/56
        """

        with open(os.path.join(
                PARENT_DIR + '/fixtures/' + "authentication_token.json")) as \
                json_data:
            self.auth_token = json.load(json_data)
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "keyword_search.json")) as \
                json_data:
            self.keyword_search_json = json.load(json_data)
        mock_return.request(
            'POST',
            AUTH_URL,
            json=self.auth_token
        )
        mock_return.request(
            'POST',
            'https://production.node.gce.gamebench.net/v1/sessions/typeahead',
            json=self.keyword_search_json['response']
        )
        creator = ModelCreator('Keyword', **KEYWORD_SEARCH_PARAMS)
        model = creator.get_model()
        expected = pandas.DataFrame(
            [self.keyword_search_json['response']]
        )
        actual = model.data

        assert_frame_equal(actual, expected)

    @requests_mock.Mocker()
    def test_filter_using_apps(self, mock_return):
        """ Keyword search using 'apps' should return the proper DataFrames.

            Regression test for https://github.com/bigfishgames/gamebenchapi-pyclient/issues/59
        """

        with open(os.path.join(
            PARENT_DIR + '/fixtures/' + "authentication_token.json")) as \
            json_data:
            self.auth_token = json.load(json_data)
        with open(os.path.join(
            PARENT_DIR + API_SAMPLES + "apps_filter.json")) as \
            json_data:
            self.app_filter_json = json.load(json_data)
        mock_return.request(
            'POST',
            AUTH_URL,
            json=self.auth_token
        )
        mock_return.request(
            'POST',
            'https://production.node.gce.gamebench.net/v1/sessions',
            json=self.app_filter_json['response']
        )
        creator = ModelCreator('SessionSummary', **APPS_FILTER_PARAMS)
        model = creator.get_model()
        expected = pandas.DataFrame(
            [self.app_filter_json['response']]
        )
        actual = model.data

        assert_frame_equal(actual, expected)
