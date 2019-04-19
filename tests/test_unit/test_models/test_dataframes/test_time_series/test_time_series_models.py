from unittest import TestCase
from unittest.mock import patch

from gamebench_api_client.models.dataframes.time_series.time_series_models import *
from tests.fixtures.constants import ABSTRACT_TIME_SERIES, DATAFRAMES_PATH


class TimeSeriesModelsTests(TestCase):

    def test_time_series_models_create(self):
        """Ensures each of the classes can be created."""
        with patch(f'{DATAFRAMES_PATH}.time_series.time_series_models.AbstractTimeSeriesModel.get_data'), \
                patch(f'{ABSTRACT_TIME_SERIES}.TimeSeriesMediator'), \
                patch(f'{ABSTRACT_TIME_SERIES}.Authenticator'):
            with self.subTest():
                battery = Battery()
                self.assertTrue(set({'metric': '/battery'}).issubset(battery.request_parameters))
            with self.subTest():
                core_frequency = CpuCoreFrequency()
                self.assertTrue(set({'metric': '/corefreq'}).issubset(core_frequency.request_parameters))
            with self.subTest():
                cpu = Cpu()
                self.assertTrue(set({'metric': '/cpu'}).issubset(cpu.request_parameters))
            with self.subTest():
                energy = Energy()
                self.assertTrue(set({'metric': '/energy'}).issubset(energy.request_parameters))
            with self.subTest():
                fps_stability = FpsStability()
                self.assertTrue(set({'metric': '/fpsStability'}).issubset(fps_stability.request_parameters))
            with self.subTest():
                fps = Fps()
                self.assertTrue(set({'metric': '/fps'}).issubset(fps.request_parameters))
            with self.subTest():
                gpu_img = GpuImg()
                self.assertTrue(set({'metric': '/gpu/img'}).issubset(gpu_img.request_parameters))
            with self.subTest():
                gpu = Gpu()
                self.assertTrue(set({'metric': '/gpu/other'}).issubset(gpu.request_parameters))
            with self.subTest():
                janks = Janks()
                self.assertTrue(set({'metric': '/janks'}).issubset(janks.request_parameters))
            with self.subTest():
                memory = Memory()
                self.assertTrue(set({'metric': '/memory'}).issubset(memory.request_parameters))
            with self.subTest():
                network = Network()
                self.assertTrue(set({'metric': '/network'}).issubset(network.request_parameters))
            with self.subTest():
                power = Power()
                self.assertTrue(set({'metric': '/power'}).issubset(power.request_parameters))
