import json
from unittest import TestCase

import requests_mock

from gamebench_api_client.models.authentication.authentication import Authenticator
from tests import *


class TestAuthentication(TestCase):
    """ Tests for the Authentication class."""

    @requests_mock.Mocker()
    def test_auth_token_returned(self, mock_return):
        """ Authenticator should assign the token dictionary to the class member 'data'."""

        with open(os.path.join(
                PARENT_DIR + API_SAMPLES + "auth_sample.json")) as \
                json_data:
            self.auth_token_json = json.load(json_data)
        mock_return.request(
            'POST',
            AUTH_URL,
            json=self.auth_token_json['response']
        )
        authenticator = Authenticator()

        expected = self.auth_token_json['response']
        actual = authenticator.data

        self.assertEqual(actual, expected)
