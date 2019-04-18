from unittest import TestCase
from gamebench_api_client.singleton import Singleton


class TestSingleton(TestCase):
    class SingletonTests(Singleton):
        pass

    def test_singleton_creation(self):
        self.SingletonTests()
