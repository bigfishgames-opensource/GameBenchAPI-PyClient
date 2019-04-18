from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.api.response.response_mediator import AuthenticationMediator, \
    GenericMediator, ResponseMediator, SessionDetailMediator, TimeSeriesMediator
from tests import *


class DefaultResponseMediator(ResponseMediator):
    """ Set up the ResponseMediator for tests."""

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)

    def get_results(self):
        """ Setup the get_results method for tests."""

        super().get_results()


class TestResponseMediator(TestCase):
    """ Tests for the ResponseMediator class."""

    def setUp(self):
        test_dict = {
            'test': 'dict'
        }
        self.mediator = DefaultResponseMediator(**test_dict)

    def test_set_data_attributes(self):
        """ Verify the get_results method exists."""

        self.mediator.get_results()


class TestSessionDetailMediator(TestCase):
    """ Unit tests for the SessionDetailMediator."""

    @patch(SESSION_RESPONSE_RETRIEVER_PATH)
    def test_init_creates_retriever(self, mock_retriever):
        """ Verify the init calls the ResponseRetriever and assigns it to a variable."""

        mediator = SessionDetailMediator(**DEFAULT_SESSION_DETAIL_PARAMS)
        with self.subTest():
            mock_retriever.assert_called_once_with(**DEFAULT_SESSION_DETAIL_PARAMS)
        with self.subTest():
            self.assertIsNotNone(mediator.retriever)

    @patch('gamebench_api_client.api.response.response_mediator.session_detail_to_dataframe')
    @patch(SESSION_RESPONSE_RETRIEVER_PATH)
    def test_set_data(self, mock_retriever, mock_utility):
        """ Verify the proper methods are called."""

        mock_retriever.get_response_json.return_value = SAMPLE_RESPONSE
        mock_utility.return_value = {
            'metric': NO_METRIC_REQUEST_PARAMS['metric'],
            'response_json': SAMPLE_RESPONSE
        }
        mediator = SessionDetailMediator(**DEFAULT_SESSION_DETAIL_PARAMS)
        mediator.get_results()

        with self.subTest():
            mock_retriever.assert_called_once_with(**DEFAULT_SESSION_DETAIL_PARAMS)
        with self.subTest():
            mock_utility.assert_called_once()


class TestGenericFrameMediator(TestCase):
    """ Unit tests for the GenericMediator."""

    @patch(SESSION_RESPONSE_RETRIEVER_PATH)
    def test_init_creates_retriever(self, mock_retriever):
        """ Verify the init calls the ResponseRetriever and assigns it to a variable."""

        mediator = GenericMediator()
        with self.subTest():
            mock_retriever.assert_called_once_with()
        self.assertIsNotNone(mediator.retriever)

    @patch('gamebench_api_client.api.response.response_mediator.to_dataframe')
    @patch(SESSION_RESPONSE_RETRIEVER_PATH)
    def test_set_data(self, mock_retriever, mock_utility):
        """ Verify the proper methods are called."""

        mock_retriever.get_response_json.return_value = SAMPLE_RESPONSE
        mediator = GenericMediator(**NO_METRIC_REQUEST_PARAMS)
        mediator.get_results()

        with self.subTest():
            mock_retriever.assert_called_once()
        mock_utility.assert_called_once()


class TestTimeSeriesMediator(TestCase):
    """ Unit tests for the TimeSeriesMediator."""

    @patch(SESSION_RESPONSE_RETRIEVER_PATH)
    def test_init_creates_retriever(self, mock_retriever):
        """ Verify the init calls the ResponseRetriever and assigns it to a variable."""

        mediator = TimeSeriesMediator()
        with self.subTest():
            mock_retriever.assert_called_once_with()
        self.assertIsNotNone(mediator.retriever)

    @patch('gamebench_api_client.api.response.response_mediator.json_to_normalized_dataframe')
    @patch(SESSION_RESPONSE_RETRIEVER_PATH)
    def test_set_data(self, mock_retriever, mock_utility):
        """ Verify the proper methods are called."""

        mock_retriever.get_response_json.return_value = SAMPLE_RESPONSE
        mediator = TimeSeriesMediator(**NO_METRIC_REQUEST_PARAMS)
        mediator.get_results()

        with self.subTest():
            mock_retriever.assert_called_once()
        mock_utility.assert_called_once()


class TestAuthenticationMediator(TestCase):
    """ Unit tests for the AuthenticationMediator."""

    @patch('gamebench_api_client.api.response.response_mediator.AuthResponseRetriever')
    def test_init_creates_retriever(self, mock_retriever):
        """ The init instantiates the AuthResponseRetriever and assigns it to a variable."""

        mediator = AuthenticationMediator()
        with self.subTest():
            mock_retriever.assert_called_once_with()
        self.assertIsNotNone(mediator.retriever)

    @patch('gamebench_api_client.api.response.response_mediator.AuthResponseRetriever')
    def test_set_data(self, mock_retriever):
        """ Verify the proper methods are called."""

        mock_retriever.get_response_json.return_value = SAMPLE_RESPONSE
        mediator = AuthenticationMediator(**NO_METRIC_REQUEST_PARAMS)
        mediator.get_results()

        with self.subTest():
            mock_retriever.assert_called_once()
