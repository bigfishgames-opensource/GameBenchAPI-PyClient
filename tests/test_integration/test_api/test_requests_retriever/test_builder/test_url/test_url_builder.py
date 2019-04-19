"""Integration tests for the authentication API."""

from unittest import TestCase

from gamebench_api_client.api.requests_retriever.builder.url.url_builder import AuthURL, \
    SessionURL
from gamebench_api_client.api.requests_retriever.builder.url.url_director import \
    URLDirector
from tests import *


class TestUrlDirector(TestCase):
    """Class for testing the url_factory."""

    def test_build_auth_url(self):
        """ Test to check that the auth URL is built correctly."""

        auth = AuthURL()
        url_director = URLDirector()
        url_director.construct_url(auth)

        expected = AUTH_URL
        actual = auth.url

        self.assertEqual(
            expected,
            actual
        )

    def test_build_session_url(self):
        """ Test to check that the session URL is build correctly."""

        session_parameters = {
            "session_id": SESSION_ID,
            "metric": METRIC
        }

        session = SessionURL()
        url_director = URLDirector()
        url_director.construct_url(session, **session_parameters)

        expected = DEFAULT_SESSION_URL
        actual = session.url

        self.assertEqual(
            expected,
            actual
        )
