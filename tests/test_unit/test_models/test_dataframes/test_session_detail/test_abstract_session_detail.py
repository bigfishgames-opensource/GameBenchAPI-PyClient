from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.models.dataframes.session_detail.abstract_session_detail import AbstractSessionDetailModel


class TestSessionDetailModel(TestCase):
    """ Unit tests for the AbstractSessionDetailModel class."""

    @patch('gamebench_api_client.models.dataframes.generic.abstract_generic.Authenticator')
    @patch(
            'gamebench_api_client.models.dataframes.session_detail.abstract_session_detail.AbstractSessionDetailModel'
            '.get_data')
    @patch('gamebench_api_client.models.dataframes.session_detail.abstract_session_detail.SessionDetailMediator')
    def test_init_sets_attributes(self, mock_session_detail, mock_get_data, mock_authenticator):
        """ Verify the instance variables call the appropriate methods."""

        test_data = {
            'metric': 'Testing'
        }
        AbstractSessionDetailModel(**test_data)

        with self.subTest():
            mock_session_detail.assert_called_with(**test_data)
        with self.subTest():
            mock_get_data.assert_called_with()
        with self.subTest():
            mock_authenticator.assert_called_with(**test_data)

    @patch('gamebench_api_client.models.dataframes.session_detail.abstract_session_detail.SessionDetailMediator')
    def test_get_data(self, mock_session_detail):
        """ Verify the data is properly set."""

        expected = "Test Data"
        mock_instance = mock_session_detail.return_value
        mock_instance.get_results.return_value = expected
        actual = AbstractSessionDetailModel().data

        self.assertEqual(
                expected,
                actual
        )
