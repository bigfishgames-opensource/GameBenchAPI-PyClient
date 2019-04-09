from unittest import TestCase
from unittest.mock import MagicMock, patch

from gamebench_api_client.api.response.response_mediator import AuthResponseRetriever, AuthenticationMediator, \
    GenericMediator, ResponseMediator, ResponseRetriever, SessionDetailMediator, TimeSeriesMediator
from gamebench_api_client.tests.fixtures.constants import NO_METRIC_REQUEST_PARAMS, SAMPLE_RESPONSE, \
    SESSION_RESPONSE_RETRIEVER_PATH


class DefaultResponseMediator(ResponseMediator):
    """ Set up the ResponseMediator for tests."""

    def __init__(self):
        super().__init__()

    def get_data(self, **request_parameters):
        """ Setup the get_data method for tests."""

        super().get_data()


class TestResponseMediator(TestCase):
    """ Tests for the ResponseMediator class."""

    def setUp(self):
        self.mediator = DefaultResponseMediator()

    def test_set_data_attributes(self):
        """ Verify the get_data method exists and accepts kwargs."""

        test_dict = {
            'test': 'dict'
        }
        self.mediator.get_data(**test_dict)


class TestSessionDetailMediator(TestCase):
    """ Unit tests for the SessionDetailMediator."""

    @patch(SESSION_RESPONSE_RETRIEVER_PATH)
    def test_init_creates_retriever(self, mock_retriever):
        """ Verify the init calls the ResponseRetriever and assigns it to a variable."""

        mediator = SessionDetailMediator()
        with self.subTest():
            mock_retriever.assert_called_once_with()
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
        mediator = SessionDetailMediator()
        mediator.get_data(**NO_METRIC_REQUEST_PARAMS)

        with self.subTest():
            mock_retriever.assert_called_once()
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
        mediator = GenericMediator()
        mediator.get_data(**NO_METRIC_REQUEST_PARAMS)

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
        mediator = TimeSeriesMediator()
        mediator.get_data(**NO_METRIC_REQUEST_PARAMS)

        with self.subTest():
            mock_retriever.assert_called_once()
        mock_utility.assert_called_once()


class TestResponseRetriever(TestCase):
    """ Unit tests for the ResponseRetriever."""

    @patch('gamebench_api_client.api.response.response_mediator.RequestDirector')
    def test_init_creates_retriever(self, mock_director):
        """ Verify the init calls the RequestDirector and assigns it to a variable."""

        retriever = ResponseRetriever()
        with self.subTest():
            mock_director.assert_called_once_with()
        self.assertIsNotNone(retriever.director)

    @patch('gamebench_api_client.api.response.response_mediator.RequestsAdapter')
    @patch('gamebench_api_client.api.response.response_mediator.RequestDirector', autospec=True)
    def test_get_response_json(self, mock_director, mock_adapter):
        """ Verify the correct methods are called and the expected json is returned."""

        test_data = {"test": "test"}

        director_mock = MagicMock()
        mock_director.return_value = director_mock
        retriever = ResponseRetriever()

        adapter_mock = MagicMock()
        mock_adapter.return_value = adapter_mock

        mock_response = MagicMock()
        mock_response.json.return_value = test_data
        adapter_mock.request.return_value = mock_response

        expected = mock_response.json.return_value
        actual = retriever.get_response_json(**test_data)

        with self.subTest():
            mock_director.assert_called_once_with()
        with self.subTest():
            mock_adapter.assert_called_once()
        with self.subTest():
            director_mock.get_session_request.assert_called_once_with(**test_data)
        with self.subTest():
            self.assertEqual(
                    expected,
                    actual
            )


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
        mediator = AuthenticationMediator()
        mediator.get_data(**NO_METRIC_REQUEST_PARAMS)

        with self.subTest():
            mock_retriever.assert_called_once()


class TestAuthResponseRetriever(TestCase):
    """ Unit tests for the ResponseRetriever."""

    @patch('gamebench_api_client.api.response.response_mediator.RequestDirector')
    def test_init_creates_retriever(self, mock_director):
        """ The init calls the RequestDirector and assigns it to a variable."""

        retriever = AuthResponseRetriever()
        with self.subTest():
            mock_director.assert_called_once_with()
        self.assertIsNotNone(retriever.director)

    @patch('gamebench_api_client.api.response.response_mediator.RequestsAdapter')
    @patch('gamebench_api_client.api.response.response_mediator.RequestDirector', autospec=True)
    def test_get_response_json(self, mock_director, mock_adapter):
        """ The correct methods are called and the expected json is returned."""

        test_data = {"test": "test"}

        director_mock = MagicMock()
        mock_director.return_value = director_mock
        retriever = AuthResponseRetriever()

        adapter_mock = MagicMock()
        mock_adapter.return_value = adapter_mock

        mock_response = MagicMock()
        mock_response.json.return_value = test_data
        adapter_mock.request.return_value = mock_response

        expected = mock_response.json.return_value
        actual = retriever.get_response_json(**test_data)

        with self.subTest():
            mock_director.assert_called_once_with()
        with self.subTest():
            mock_adapter.assert_called_once()
        with self.subTest():
            director_mock.get_auth_request.assert_called_once_with(**test_data)
        with self.subTest():
            self.assertEqual(
                    expected,
                    actual
            )
