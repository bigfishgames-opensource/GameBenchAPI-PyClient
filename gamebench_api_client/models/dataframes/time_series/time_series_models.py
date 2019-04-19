""" All modules that use the TimeSeriesMediator.

    The classes inherit from the AbstractTimeSeriesModel.
    Each model is kept as its own class so new behavior can be added
    individually as needed.
"""

from gamebench_api_client.models.dataframes.time_series.abstract_time_series import AbstractTimeSeriesModel


class Battery(AbstractTimeSeriesModel):
    """ Object to set the Battery information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/battery"


class CpuCoreFrequency(AbstractTimeSeriesModel):
    """ Object to set the CPU Core Frequency information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/corefreq"


class Cpu(AbstractTimeSeriesModel):
    """ Object to set the CPU usage information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/cpu"


class Energy(AbstractTimeSeriesModel):
    """ Object to set the Energy information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/energy"


class FpsStability(AbstractTimeSeriesModel):
    """ Object to set the FPS Stability information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/fpsStability"


class Fps(AbstractTimeSeriesModel):
    """ Object to set the FPS information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/fps"


class GpuImg(AbstractTimeSeriesModel):
    """ Object to set the Imagination GPU information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/gpu/img"


class Gpu(AbstractTimeSeriesModel):
    """ Object to set the non-Imagination GPU information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/gpu/other"


class Janks(AbstractTimeSeriesModel):
    """ Object to set the Janks information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/janks"


class Memory(AbstractTimeSeriesModel):
    """ Object to set the Memory information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/memory"


class Network(AbstractTimeSeriesModel):
    """ Object to set the Network information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/network"


class Power(AbstractTimeSeriesModel):
    """ Object to set the Power information for a session."""

    def __init__(self):
        super().__init__()
        self.request_parameters["metric"] = "/power"
