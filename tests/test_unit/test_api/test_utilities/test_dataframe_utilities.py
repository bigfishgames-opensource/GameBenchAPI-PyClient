import json
from unittest import TestCase

import pandas
from pandas.io.json import json_normalize
from pandas.util.testing import assert_frame_equal

from gamebench_api_client.api.utilities.dataframe_utilities import \
    json_to_normalized_dataframe, session_detail_to_dataframe, to_dataframe
from tests import *


class TestDataFrameUtilities(TestCase):

    def setUp(self):
        self.data_frame = pandas.DataFrame()
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "gpu_img.json")) as json_data:
            self.test_json = json.load(json_data)
        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "sessionid.json")) as json_data:
            self.session_json = json.load(json_data)

    def test_json_to_normalized_dataframe(self):
        """ Verify a DataFrame is returned after normalizing a JSON."""

        expected = json_normalize(
            self.test_json['response'],
            'samples',
            ['id', 'sessionId']
        )
        actual = json_to_normalized_dataframe(self.test_json['response'])

        assert_frame_equal(
            expected,
            actual
        )

    def test_session_metric_to_dataframe(self):
        """ Verify a DataFrame is returned when given a specific metric."""

        expected = pandas.DataFrame(data=[self.session_json['response']['app']])
        actual = session_detail_to_dataframe('app', self.session_json['response'])

        assert_frame_equal(
            expected,
            actual
        )

    def test_to_dataframe(self):
        """ Verify a DataFrame is returned when given an array."""

        expected = pandas.DataFrame(self.test_json)
        actual = to_dataframe(self.test_json)

        assert_frame_equal(
            expected,
            actual
        )
