from unittest import TestCase

from gamebench_api_client.global_settings import GAMEBENCH_CONFIG
from gamebench_api_client.global_settings import set_api_endpoint, get_username_and_password


class TestSetAPIEndpoint(TestCase):
    """ Tests for the set_api_endpoint function."""

    def test_endpoint_returned(self):
        """ Verify the set_api_endpoint function returns the full api endpoint.

            The full end-point should be the result of concatenating the url and
            api_version from the GAMEBENCH_CONFIG dictionary.
        """
        actual = set_api_endpoint()
        expected = 'https://production.node.gce.gamebench.net/v1'
        self.assertEqual(actual, expected)

    def test_get_username_and_password(self):
        """ The username and password is returned as a dictionary, using values from GAMEBENCH_CONFIG."""
        expected = {"username": GAMEBENCH_CONFIG['username'], "password": GAMEBENCH_CONFIG['password']}
        actual = get_username_and_password()
        self.assertEqual(expected, actual)
