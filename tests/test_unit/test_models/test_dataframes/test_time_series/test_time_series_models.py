from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.models.dataframes.time_series.time_series_models import *
from tests.fixtures.constants import ABSTRACT_TIME_SERIES, DATAFRAMES_PATH


class TimeSeriesModelsTests(TestCase):

    def test_time_series_models_create(self):
        """Ensures each of the classes can be created."""
        with patch(f'{DATAFRAMES_PATH}.time_series.time_series_models.AbstractTimeSeriesModel.get_data'),\
                patch(f'{ABSTRACT_TIME_SERIES}.TimeSeriesMediator'),\
                patch(f'{ABSTRACT_TIME_SERIES}.Authenticator'):
            with self.subTest():
                Battery()
            with self.subTest():
                CpuCoreFrequency()
            with self.subTest():
                Cpu()
            with self.subTest():
                Energy()
            with self.subTest():
                FpsStability()
            with self.subTest():
                Fps()
            with self.subTest():
                GpuImg()
            with self.subTest():
                Gpu()
            with self.subTest():
                Janks()
            with self.subTest():
                Memory()
            with self.subTest():
                Network()
            with self.subTest():
                Power()
