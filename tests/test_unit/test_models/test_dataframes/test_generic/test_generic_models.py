from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.models.dataframes.generic.generic_models import *
from tests.fixtures.constants import ABSTRACT_GENERIC, DATAFRAMES_PATH


class GenericModelsTests(TestCase):

    def test_generic_models_create(self):
        """Ensures each of the classes can be created."""

        with patch(f'{DATAFRAMES_PATH}.generic.generic_models.AbstractGenericModel.get_data'), \
                patch(f'{ABSTRACT_GENERIC}.GenericMediator'), \
                patch(f'{ABSTRACT_GENERIC}.Authenticator'):
            with self.subTest():
                keyword = Keyword()
                self.assertEqual('/typeahead', keyword.request_parameters['metric'])
            with self.subTest():
                markers = Markers()
                self.assertEqual('/markers', markers.request_parameters['metric'])
            with self.subTest():
                notes = SessionNotes()
                self.assertEqual('/notes', notes.request_parameters['metric'])
            with self.subTest():
                summary = SessionSummary()
                self.assertEqual('', summary.request_parameters['metric'])

    def test_session_detail_attributes(self):
        """ Ensures the class attributes for SessionSummary are created."""

        with patch(f'{DATAFRAMES_PATH}.generic.generic_models.AbstractGenericModel.get_data'), \
                patch(f'{ABSTRACT_GENERIC}.GenericMediator'), \
                patch(f'{ABSTRACT_GENERIC}.Authenticator'):
            with self.subTest():
                summary = SessionSummary()
                with self.subTest():
                    self.assertIsNotNone(summary.app)
                with self.subTest():
                    self.assertIsNotNone(summary.device)
                with self.subTest():
                    self.assertIsNotNone(summary.location)
                with self.subTest():
                    self.assertIsNotNone(summary.metrics)
                with self.subTest():
                    self.assertIsNotNone(summary.network_app_usage)
