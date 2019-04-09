""" All modules that use the TimeSeriesMediator.

    The classes inherit from the AbstractTimeSeriesModel.
    Each model is kept as its own class so new behavior can be added
    individually as needed.
"""

from gamebench_api_client.models.dataframes.time_series.abstract_time_series import AbstractTimeSeriesModel


class Battery(AbstractTimeSeriesModel):
    """ Object to set the Battery information for a session."""

    pass


class CpuCoreFrequency(AbstractTimeSeriesModel):
    """ Object to set the CPU Core Frequency information for a session."""

    pass


class Cpu(AbstractTimeSeriesModel):
    """ Object to set the CPU usage information for a session."""

    pass


class Energy(AbstractTimeSeriesModel):
    """ Object to set the Energy information for a session."""

    pass


class FpsStability(AbstractTimeSeriesModel):
    """ Object to set the FPS Stability information for a session."""

    pass


class Fps(AbstractTimeSeriesModel):
    """ Object to set the FPS information for a session."""

    pass


class GpuImg(AbstractTimeSeriesModel):
    """ Object to set the Imagination GPU information for a session."""

    pass


class Gpu(AbstractTimeSeriesModel):
    """ Object to set the non-Imagination GPU information for a session."""

    pass


class Janks(AbstractTimeSeriesModel):
    """ Object to set the Janks information for a session."""

    pass


class Memory(AbstractTimeSeriesModel):
    """ Object to set the Memory information for a session."""

    pass


class Network(AbstractTimeSeriesModel):
    """ Object to set the Network information for a session."""

    pass


class Power(AbstractTimeSeriesModel):
    """ Object to set the Power information for a session."""

    pass
