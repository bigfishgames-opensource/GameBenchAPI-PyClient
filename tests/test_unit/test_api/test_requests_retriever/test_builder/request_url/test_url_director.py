"""Unit tests for the URL Director module."""

from unittest import TestCase

from gamebench_api_client.api.requests_retriever.builder.url.url_director import URLDirector


class TestURLDirector(TestCase):
    """ Class responsible for testing the URL Builder class."""

    def setUp(self):
        self.url_director = URLDirector()

    def test_init_sets_builder_to_none(self):
        """ Test the _builder is set to none on instantiation."""

        self.assertEqual(
            self.url_director._builder,
            None
        )
