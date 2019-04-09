""" The Authenticator class should be calling the appropriate methods."""

from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.models.authentication.authentication import Authenticator


class TestAuthenticator(TestCase):
    """ Unit tests for the Authenticator class."""

    @patch('gamebench_api_client.models.authentication.authentication.Authenticator.get_data')
    @patch('gamebench_api_client.models.authentication.authentication.AuthenticationMediator')
    def test_init_sets_attributes(self, mock_mediator, mock_get_data):
        """ The instance variables call the appropriate methods."""

        test_data = {
            'username': 'Testing',
            'password': 'Blah'
        }
        Authenticator(**test_data)

        with self.subTest():
            mock_mediator.assert_called_with()
        with self.subTest():
            mock_get_data.assert_called_with(**test_data)

    @patch('gamebench_api_client.models.authentication.authentication.AuthenticationMediator')
    def test_get_data(self, mock_mediator):
        """ The data variable is properly set."""

        expected = "Test Data"
        mock_instance = mock_mediator.return_value
        mock_instance.get_data.return_value = expected
        actual = Authenticator().data

        self.assertEqual(
                expected,
                actual
        )
