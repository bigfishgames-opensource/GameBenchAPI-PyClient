from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.models.dataframes.generic.abstract_generic import AbstractGenericModel


class TestGenericFrameModel(TestCase):
    """ Unit tests for the AbstractGenericModel class."""

    @patch('gamebench_api_client.models.dataframes.generic.abstract_generic.Authenticator')
    @patch('gamebench_api_client.models.dataframes.generic.abstract_generic.AbstractGenericModel.get_data')
    @patch('gamebench_api_client.models.dataframes.generic.abstract_generic.GenericMediator')
    def test_init_sets_attributes(self, mock_generic_frame, mock_get_data, mock_authenticator):
        """ Verify the instance variables call the appropriate methods."""

        test_data = {
            'metric': 'Testing'
        }
        generic_model = AbstractGenericModel(**test_data)

        with self.subTest():
            mock_generic_frame.assert_called_with(generic_model.request_parameters)
        with self.subTest():
            mock_get_data.assert_called_with()
        with self.subTest():
            mock_authenticator.assert_called_with(**test_data)

    @patch('gamebench_api_client.models.dataframes.generic.abstract_generic.GenericMediator')
    def test_get_data(self, mock_generic_frame):
        """ Verify the data is properly set."""

        expected = "Test Data"
        mock_instance = mock_generic_frame.return_value
        mock_instance.get_results.return_value = expected

        with patch('gamebench_api_client.models.dataframes.generic.abstract_generic.Authenticator'):
            actual = AbstractGenericModel().data

        self.assertEqual(
                expected,
                actual
        )
