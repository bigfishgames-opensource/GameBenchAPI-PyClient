from unittest import TestCase

from gamebench_api_client.singleton import Singleton


class SingletonStub(Singleton):
    """Stub Singleton for test setup."""

    def __init__(self):
        super().__init__()
        self.singleton_property = None

    def set_property(self, property_input):
        self.singleton_property = property_input


class TestSingleton(TestCase):
    """Testing the base Singleton"""

    def test_singleton_pattern(self):
        """The Stub should be a singleton, ensures all objects are the same."""
        singleton_1 = SingletonStub()
        singleton_1.set_property("first")

        singleton_2 = SingletonStub()
        singleton_2.set_property("second")

        self.assertIs(singleton_1, singleton_2)
