from unittest import TestCase
from unittest.mock import patch, Mock

from gamebench_api_client.models.dataframes.session_detail.abstract_session_detail import AbstractSessionDetailModel
from tests.fixtures.constants import ABSTRACT_SESSION_DETAIL


class TestSessionDetailModel(TestCase):
    """ Unit tests for the AbstractSessionDetailModel class."""

    @patch(f'{ABSTRACT_SESSION_DETAIL}.Authenticator')
    @patch(f'{ABSTRACT_SESSION_DETAIL}.AbstractSessionDetailModel.get_data')
    @patch(f'{ABSTRACT_SESSION_DETAIL}.SessionDetailMediator')
    def test_init_sets_attributes(self, mock_session_detail, mock_get_data, mock_authenticator):
        """ Verify the instance variables call the appropriate methods."""

        session_detail_model = AbstractSessionDetailModel()

        with self.subTest():
            mock_session_detail.assert_called_with(**session_detail_model.request_parameters)
        with self.subTest():
            mock_get_data.assert_called_with()
        with self.subTest():
            mock_authenticator.assert_called_with()

    @patch(f'{ABSTRACT_SESSION_DETAIL}.SessionDetailMediator')
    def test_get_data(self, mock_session_detail):
        """ Verify the data is properly set."""

        expected = "Test Data"
        mock_instance = mock_session_detail.return_value
        mock_instance.get_results.return_value = expected

        with patch(f'{ABSTRACT_SESSION_DETAIL}.Authenticator'):
            actual = AbstractSessionDetailModel().data

        self.assertEqual(
            expected,
            actual
        )

    @patch(f'{ABSTRACT_SESSION_DETAIL}.Authenticator')
    def test_auth_token_added_to_request_parameters(self, mock_authenticator):
        """ Ensure that the Authenticator token is added to the request_parameters dictionary as 'auth_token'."""

        expected_dict = {
            'auth_token': 'q1w2e3r4t5y6'
        }
        mock_dict = Mock()
        mock_dict.data = {
            'token': 'q1w2e3r4t5y6'
        }
        mock_authenticator.return_value = mock_dict

        with patch(f'{ABSTRACT_SESSION_DETAIL}.SessionDetailMediator'), \
                patch(f'{ABSTRACT_SESSION_DETAIL}.AbstractSessionDetailModel.get_data'):
            actual = AbstractSessionDetailModel()

        self.assertDictEqual(expected_dict, actual.request_parameters)
