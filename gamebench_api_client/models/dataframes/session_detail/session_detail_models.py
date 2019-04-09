""" All modules that use the SessionDetailMediator.

    The classes inherit from the AbstractSessionDetailModel.
    Each model is kept as its own class so new behavior can be added
    individually as needed.
"""

from gamebench_api_client.models.dataframes.session_detail.abstract_session_detail import AbstractSessionDetailModel


class App(AbstractSessionDetailModel):
    """ Object to set the App detail for a session."""

    pass


class Device(AbstractSessionDetailModel):
    """ Object to set the Device detail for a session."""

    pass


class Location(AbstractSessionDetailModel):
    """ Object to set the Location detail for a session."""

    pass


class Metrics(AbstractSessionDetailModel):
    """ Object to set the Metrics detail for a session."""

    pass


class NetworkUsage(AbstractSessionDetailModel):
    """ Object to set the Network Usage detail for a session."""

    pass
