"""Integration tests for the authentication API."""

from unittest import TestCase

from gamebench_api_client.api.requests_retriever.builder.url.url_director import \
    URLDirector
from tests import *


class TestGetUrl(TestCase):
    def test_get_auth_url(self):
        """ Test to check that get_auth_url returns the auth URL string."""

        url_builder = URLDirector()

        expected = AUTH_URL
        actual = url_builder.get_auth_url()

        self.assertEqual(
            expected,
            actual
        )

    def test_get_session_url(self):
        """ Test to check that get_session_url returns the session URL string."""
        session_parameters = {
            "session_id": SESSION_ID,
            "metric": METRIC
        }

        url_builder = URLDirector()

        expected = DEFAULT_SESSION_URL
        actual = url_builder.get_session_url(**session_parameters)

        self.assertEqual(
            expected,
            actual
        )
