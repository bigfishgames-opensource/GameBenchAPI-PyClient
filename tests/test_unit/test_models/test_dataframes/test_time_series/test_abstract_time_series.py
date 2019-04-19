from unittest import TestCase
from unittest.mock import patch, Mock

from gamebench_api_client.models.dataframes.time_series.abstract_time_series import AbstractTimeSeriesModel
from tests.fixtures.constants import ABSTRACT_TIME_SERIES


class TestAbstractTimeSeriesModel(TestCase):
    """ Unit tests for the AbstractTimeSeriesModel class."""

    @patch(f'{ABSTRACT_TIME_SERIES}.Authenticator')
    @patch(f'{ABSTRACT_TIME_SERIES}.AbstractTimeSeriesModel.get_data')
    @patch(f'{ABSTRACT_TIME_SERIES}.TimeSeriesMediator')
    def test_init_sets_attributes(self, mock_time_series, mock_get_data, mock_authenticator):
        """ Verify the instance variables call the appropriate methods."""

        time_series_model = AbstractTimeSeriesModel()

        with self.subTest():
            mock_time_series.assert_called_with(**time_series_model.request_parameters)
        with self.subTest():
            mock_get_data.assert_called_with()
        with self.subTest():
            mock_authenticator.assert_called_with()

    @patch(f'{ABSTRACT_TIME_SERIES}.TimeSeriesMediator')
    def test_get_data(self, mock_time_series):
        """ Verify the data is properly set."""

        expected = "Test Data"
        mock_instance = mock_time_series.return_value
        mock_instance.get_results.return_value = expected

        with patch(f'{ABSTRACT_TIME_SERIES}.Authenticator'):
            actual = AbstractTimeSeriesModel().data

        self.assertEqual(
            expected,
            actual
        )

    @patch(f'{ABSTRACT_TIME_SERIES}.Authenticator')
    def test_auth_token_added_to_request_parameters(self, mock_authenticator):
        """ Ensure that the Authenticator token is added to the request_parameters dictionary as 'auth_token'."""

        expected_dict = {
            'auth_token': 'q1w2e3r4t5y6',
            'metric': ''
        }
        mock_dict = Mock()
        mock_dict.data = {
            'token': 'q1w2e3r4t5y6'
        }
        mock_authenticator.return_value = mock_dict

        with patch(f'{ABSTRACT_TIME_SERIES}.TimeSeriesMediator'), \
                patch(f'{ABSTRACT_TIME_SERIES}.AbstractTimeSeriesModel.get_data'):
            actual = AbstractTimeSeriesModel()

        self.assertDictEqual(expected_dict, actual.request_parameters)
