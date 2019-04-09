from unittest import TestCase
from unittest.mock import MagicMock, patch

from gamebench_api_client.api.response.response_retriever import AbstractRetriever


class StubAbstractRetriever(AbstractRetriever):

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)

    def get_response_json(self):
        super().get_response_json()


class TestAbstractRetriever(TestCase):

    @patch('gamebench_api_client.api.response.response_retriever.RequestsAdapter')
    @patch('gamebench_api_client.api.response.response_retriever.RequestDirector')
    def test_init(self, mock_director, mock_adapter):
        mock_director.return_value = MagicMock()
        mock_adapter.return_value = 'Test'
        test_data = {"test": "test"}
        retriever = StubAbstractRetriever(**test_data)
        with self.subTest():
            self.assertEqual(retriever.request_parameters, test_data)
        with self.subTest():
            self.assertIsNotNone(retriever.director)
        with self.subTest():
            self.assertIsNone(retriever.request)
        with self.subTest():
            self.assertIsNone(retriever.adapter)
        with self.subTest():
            self.assertIsNone(retriever.response)
