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
        print(creator.instance.data)

        assert_frame_equal(actual, expected)
