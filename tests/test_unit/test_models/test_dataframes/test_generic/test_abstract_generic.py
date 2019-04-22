from unittest import TestCase
from unittest.mock import patch, Mock

from gamebench_api_client.models.dataframes.generic.abstract_generic import AbstractGenericModel
from tests.fixtures.constants import ABSTRACT_GENERIC


class TestGenericFrameModel(TestCase):
    """ Unit tests for the AbstractGenericModel class."""

    @patch(f'{ABSTRACT_GENERIC}.Authenticator')
    @patch(f'{ABSTRACT_GENERIC}.AbstractGenericModel.get_data')
    @patch(f'{ABSTRACT_GENERIC}.GenericMediator')
    def test_init_sets_attributes(self, mock_generic_frame, mock_get_data, mock_authenticator):
        """ Verify the instance variables call the appropriate methods."""

        generic_model = AbstractGenericModel()

        with self.subTest():
            mock_generic_frame.assert_called_with(**generic_model.request_parameters)
        with self.subTest():
            mock_get_data.assert_called_with()
        with self.subTest():
            mock_authenticator.assert_called_with()

    @patch(f'{ABSTRACT_GENERIC}.GenericMediator')
    def test_get_data(self, mock_generic_frame):
        """ Verify the data is properly set."""

        expected = "Test Data"
        mock_instance = mock_generic_frame.return_value
        mock_instance.get_results.return_value = expected

        with patch(f'{ABSTRACT_GENERIC}.Authenticator'):
            actual = AbstractGenericModel().data

        self.assertEqual(
            expected,
            actual
        )

    @patch(f'{ABSTRACT_GENERIC}.Authenticator')
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

        with patch(f'{ABSTRACT_GENERIC}.GenericMediator'), \
                patch(f'{ABSTRACT_GENERIC}.AbstractGenericModel.get_data'):
            actual = AbstractGenericModel()

        self.assertDictEqual(expected_dict, actual.request_parameters)
