from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.models.dataframes.time_series.abstract_time_series import AbstractTimeSeriesModel


class TestAbstractTimeSeriesModel(TestCase):
    """ Unit tests for the AbstractTimeSeriesModel class."""

    @patch('gamebench_api_client.models.dataframes.time_series.abstract_time_series.AbstractTimeSeriesModel.get_data')
    @patch('gamebench_api_client.models.dataframes.time_series.abstract_time_series.TimeSeriesMediator')
    def test_init_sets_attributes(self, mock_time_series, mock_get_data):
        """ Verify the instance variables call the appropriate methods."""

        test_data = {
            'metric': 'Testing'
        }
        AbstractTimeSeriesModel(**test_data)

        with self.subTest():
            mock_time_series.assert_called_with(**test_data)
        with self.subTest():
            mock_get_data.assert_called_with()

    @patch('gamebench_api_client.models.dataframes.time_series.abstract_time_series.TimeSeriesMediator')
    def test_get_data(self, mock_time_series):
        """ Verify the data is properly set."""

        expected = "Test Data"
        mock_instance = mock_time_series.return_value
        mock_instance.get_results.return_value = expected
        actual = AbstractTimeSeriesModel().data

        self.assertEqual(
                expected,
                actual
        )
