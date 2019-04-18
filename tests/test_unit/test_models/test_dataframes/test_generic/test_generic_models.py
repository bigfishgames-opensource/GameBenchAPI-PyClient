from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.models.dataframes.generic.generic_models import *
from tests.fixtures.constants import ABSTRACT_GENERIC, DATAFRAMES_PATH


class GenericModelsTests(TestCase):

    def test_generic_models_create(self):
        """Ensures each of the classes can be created."""
        with patch(f'{DATAFRAMES_PATH}.generic.generic_models.AbstractGenericModel.get_data'),\
                patch(f'{ABSTRACT_GENERIC}.GenericMediator'),\
                patch(f'{ABSTRACT_GENERIC}.Authenticator'):
            with self.subTest():
                Keyword()
            with self.subTest():
                Markers()
            with self.subTest():
                SessionNotes()
            with self.subTest():
                SessionSummary()
