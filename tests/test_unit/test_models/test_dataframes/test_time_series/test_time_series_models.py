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
                self.assertEqual('/battery', battery.request_parameters['metric'])
            with self.subTest():
                core_frequency = CpuCoreFrequency()
                self.assertEqual('/corefreq', core_frequency.request_parameters['metric'])
            with self.subTest():
                cpu = Cpu()
                self.assertEqual('/cpu', cpu.request_parameters['metric'])
            with self.subTest():
                energy = Energy()
                self.assertEqual('/energy', energy.request_parameters['metric'])
            with self.subTest():
                fps_stability = FpsStability()
                self.assertEqual('/fpsStability', fps_stability.request_parameters['metric'])
            with self.subTest():
                fps = Fps()
                self.assertEqual('/fps', fps.request_parameters['metric'])
            with self.subTest():
                gpu_img = GpuImg()
                self.assertEqual('/gpu/img', gpu_img.request_parameters['metric'])
            with self.subTest():
                gpu = Gpu()
                self.assertEqual('/gpu/other', gpu.request_parameters['metric'])
            with self.subTest():
                janks = Janks()
                self.assertEqual('/janks', janks.request_parameters['metric'])
            with self.subTest():
                memory = Memory()
                self.assertEqual('/memory', memory.request_parameters['metric'])
            with self.subTest():
                network = Network()
                self.assertEqual('/network', network.request_parameters['metric'])
            with self.subTest():
                power = Power()
                self.assertEqual('/power', power.request_parameters['metric'])
