import json
from unittest import TestCase

import pandas
from pandas.io.json import json_normalize
from pandas.util.testing import assert_frame_equal
import requests_mock

from tests import *
from gamebench_api_client.models.creator.model_creator import ModelCreator


class TestModelCreator(TestCase):
    """ Tests for the ModelCreator class."""

    @requests_mock.Mocker()
    def test_time_series_model_creation(self, mock_return):
        """ The ModelCreator returns the proper DataFrame."""

        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "cpu_multiple_sessions.json")) as \
                json_data:
            self.time_series_json = json.load(json_data)
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
