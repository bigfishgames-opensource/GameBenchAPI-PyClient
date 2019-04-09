from unittest import TestCase
from unittest.mock import patch, Mock

from gamebench_api_client.models.creator.model_creator import ModelCreator, ModelNotFound
from tests import *


def stub_function():
    """ Use to mock the behavior of the model_class variable.

        The model_class variable returns the value of a named object
        due to the use of getattr().
    """

    return "Stub Function"


class TestModelCreator(TestCase):
    """ Unit tests for the Model Creator.

        The init calls the methods to get the proper model instance,
        so the setup needs to patch all of those methods.
    """

    @patch(MODEL_CREATOR_GET_CLASS)
    @patch(MODEL_CREATOR_IMPORT_MODULE)
    @patch(MODEL_CREATOR_SET_MODULE)
    def setUp(self, mock_module, mock_import, mock_object):
        mock_module.return_value = "Test.Path"
        mock_import.return_value = "Test Module"
        mock_object.return_value = stub_function
        self.creator = ModelCreator("Cpu")

    def test_init_creates_module_path(self):
        """ Verify the correct method is called and assigned to the module_path variable."""

        with self.subTest():
            expected = "Test.Path"
            actual = self.creator.module_path
            self.assertEqual(actual, expected)

    def test_init_creates_imported_module(self):
        """ Verify the correct method is called and assigned to the imported_module variable."""

        expected = "Test Module"
        actual = self.creator.imported_module
        self.assertEqual(actual, expected)

    def test_init_creates_model_class(self):
        """ Verify the model_class variable calls the proper method."""

        expected = stub_function
        actual = self.creator.model_class
        self.assertEqual(actual, expected)

    def test_init_creates_instance(self):
        """ Verify the instance variable is assigned."""

        expected = "Stub Function"
        actual = self.creator.instance
        self.assertEqual(actual, expected)


class TestFindGeneric(TestCase):
    """ Module path for Generic models can be found."""

    @patch(MODEL_CREATOR_GET_CLASS)
    @patch(MODEL_CREATOR_IMPORT_MODULE)
    @patch(MODEL_CREATOR_SET_MODULE)
    def setUp(self, mock_module, mock_import, mock_object):
        mock_module.return_value = "Test.Path"
        mock_import.return_value = "Test Module"
        mock_object.return_value = stub_function
        self.creator = ModelCreator("SessionSummary")

    def test_find_generic_frame_model(self):
        """ Verify a generic frame model can be found and the model name returned."""

        actual = self.creator._set_module_name_by_model()
        expected = "gamebench_api_client.models.dataframes.generic.generic_models"
        self.assertEqual(actual, expected)


class TestFindSessionDetail(TestCase):
    """ Module path for Session Detail models can be found."""

    @patch(MODEL_CREATOR_GET_CLASS)
    @patch(MODEL_CREATOR_IMPORT_MODULE)
    @patch(MODEL_CREATOR_SET_MODULE)
    def setUp(self, mock_module, mock_import, mock_object):
        mock_module.return_value = "Test.Path"
        mock_import.return_value = "Test Module"
        mock_object.return_value = stub_function
        self.creator = ModelCreator("App")

    def test_find_session_detail_model(self):
        """ Verify a session detail model can be found and the model name returned."""

        actual = self.creator._set_module_name_by_model()
        expected = "gamebench_api_client.models.dataframes.session_detail.session_detail_models"
        self.assertEqual(actual, expected)


class TestFindTimeSeries(TestCase):
    """ Module path for Time Series models can be found."""

    @patch(MODEL_CREATOR_GET_CLASS)
    @patch(MODEL_CREATOR_IMPORT_MODULE)
    @patch(MODEL_CREATOR_SET_MODULE)
    def setUp(self, mock_module, mock_import, mock_object):
        mock_module.return_value = "Test.Path"
        mock_import.return_value = "Test Module"
        mock_object.return_value = stub_function
        self.creator = ModelCreator("Cpu")

    def test_find_time_series_model(self):
        """ Verify a time series model can be found and the model name returned."""

        actual = self.creator._set_module_name_by_model()
        expected = "gamebench_api_client.models.dataframes.time_series.time_series_models"
        self.assertEqual(actual, expected)


class TestModelNotFound(TestCase):
    """ Unit tests to verify the correct error message is raised if a given model doesn't exist."""

    @patch(MODEL_CREATOR_GET_CLASS)
    @patch(MODEL_CREATOR_IMPORT_MODULE)
    def test_error_raise_when_module_not_found(self, mock_import, mock_object):
        """ Verify the ModuleNotFound exception is raised if the given model doesn't exist."""

        mock_class_object = Mock
        mock_import.return_value = 'mocking.a.module.path'
        mock_object.return_value = mock_class_object
        expected = "The not_valid model does not exist."
        with self.assertRaises(ModelNotFound) as module_error:
            self.creator = ModelCreator("not_valid")
        actual = str(module_error.exception)
        self.assertEqual(actual, expected)
