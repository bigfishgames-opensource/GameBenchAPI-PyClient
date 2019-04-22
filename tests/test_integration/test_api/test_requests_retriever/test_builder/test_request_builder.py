""" Integration tests for the Request Builder."""

from unittest import TestCase

from gamebench_api_client.api.requests_retriever.builder.request_builder import AuthRequest, \
    SessionRequest
from gamebench_api_client.api.requests_retriever.builder.request_director import RequestDirector
from tests import *


class TestRequestBuilder(TestCase):
    """ Tests for the Request Builder."""

    def setUp(self):
        self.request_director = RequestDirector()

    def test_auth_request(self):
        """ Test to check that each property of the auth request is
            built and set correctly.
        """

        auth = AuthRequest(**AUTH_DATA)
        self.request_director.construct_request(auth)

        expected = {
            "method": "POST",
            "url": AUTH_URL,
            "headers": AUTH_HEADERS,
            "data": AUTH_DATA
        }
        actual = {
            "method": auth.request.method,
            "url": auth.request.url,
            "headers": auth.request.headers,
            "data": auth.request.data
        }

        self.assertEqual(
            expected,
            actual
        )

    def test_basic_session_request(self):
        """ Test to check that each property of the auth request is
            built and set correctly.
        """

        request_parameters = DEFAULT_REQUEST_PARAMS

        session = SessionRequest(**request_parameters)
        self.request_director.construct_request(session)

        expected = {
            "method": "GET",
            "url": DEFAULT_SESSION_URL,
            "headers": DEFAULT_SESSION_HEADERS,
            "params": "test_params",
            "data": {
                "test_data": "test_data"
            }
        }
        actual = {
            "method": session.request.method,
            "url": session.request.url,
            "headers": session.request.headers,
            "params": session.request.params,
            "data": session.request.data
        }

        self.assertEqual(
            expected,
            actual
        )
