from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.models.dataframes.session_detail.session_detail_models import *
from tests.fixtures.constants import ABSTRACT_SESSION_DETAIL, DATAFRAMES_PATH


class SessionDetailModelsTests(TestCase):

    def test_session_detail_models_create(self):
        """Ensures each of the classes can be created."""
        with patch(f'{DATAFRAMES_PATH}.session_detail.session_detail_models.AbstractSessionDetailModel.get_data'),\
                patch(f'{ABSTRACT_SESSION_DETAIL}.SessionDetailMediator'),\
                patch(f'{ABSTRACT_SESSION_DETAIL}.Authenticator'):
            with self.subTest():
                App()
            with self.subTest():
                Device()
            with self.subTest():
                Location()
            with self.subTest():
                Metrics()
            with self.subTest():
                NetworkUsage()
