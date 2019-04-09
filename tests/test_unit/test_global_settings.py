from unittest import TestCase

from gamebench_api_client.global_settings import set_api_endpoint


class TestSetAPIEndpoint(TestCase):
    """ Tests for the set_api_endpoint function."""

    def test_endpoint_returned(self):
        """ Verify the set_api_endpoint function returns the full api endpoint.
        
            The full end-point should be the result of concatenating the url and
            api_version from the GAMEBENCH_CONFIG dictionary.
        """
        actual = set_api_endpoint()
        expected = 'https://api.production.gamebench.net/v1'
        self.assertEqual(actual, expected)
