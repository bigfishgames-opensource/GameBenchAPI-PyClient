""" Unit tests for the Adapter."""

from unittest import TestCase

import requests_mock

from gamebench_api_client.api.requests_retriever.request_adapter.adapter import Adapter, \
    RequestsAdapter
from tests import *


class DefaultAdapter(Adapter):
    """ Creating a default test class to verify abstract functionality."""

    def __init__(self):
        """ Default implementation of the interface's init."""

        super().__init__()

    def request(self):
        """ Default implementation of the request method."""

        super().request()


class TestAdapterInterface(TestCase):
    """ Class to verify the Adapter Interface is set up correctly."""

    def setUp(self):
        self.adapter = DefaultAdapter()

    def test_init_sets_http_library(self):
        """ Verify the init creates a _http_library object."""

        self.assertEqual(self.adapter._http_library, None)

    def test_request(self):
        """ Verify the request method can be called."""

        self.assertEqual(self.adapter.request(), None)


class TestRequestsAdapter(TestCase):
    """ Class to test the adapter for the Requests library."""

    @requests_mock.Mocker()
    def test_auth_request(self, mock_return):
        """ Verify that an auth token is returned when request is sent with auth attributes."""

        adapter = RequestsAdapter(**AUTH_ATTRIBUTES)
        mock_return.request(
            "POST",
            AUTH_URL,
            json={
                "token": "test_token"
            }
        )

        response = adapter.request()
        json_response = response.json()
        self.assertEqual(json_response["token"], "test_token")

    @requests_mock.Mocker()
    def test_session_request(self, mock_return):
        """ Verify that a session object is returned in a GET request."""

        adapter = RequestsAdapter(**SESSION_ATTRIBUTES)
        mock_return.request(
            "GET",
            DEFAULT_SESSION_URL,
            json={
                "id": "test_id",
                "app": {
                    "name": "EtherPad",
                    "version": 1,
                    "packageName": "com.test.testios"
                }
            }
        )

        response = adapter.request()
        json_response = response.json()
        self.assertEqual(json_response["id"], "test_id")
