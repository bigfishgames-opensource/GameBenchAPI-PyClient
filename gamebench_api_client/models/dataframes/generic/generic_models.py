""" All modules that use the GenericMediator.

    The classes inherit from the AbstractGenericModel.
    Each model is kept as its own class so new behavior can be added
    individually as needed.
"""

from gamebench_api_client.models.dataframes.generic.abstract_generic import AbstractGenericModel


class Keyword(AbstractGenericModel):
    """ Object to set the results for a keyword search."""

    METRIC_PATH = '/typeahead'


class Markers(AbstractGenericModel):
    """ Object to set the Markers information for a session."""

    METRIC_PATH = '/markers'


class SessionNotes(AbstractGenericModel):
    """ Object to set the Session Notes for a session."""

    METRIC_PATH = '/notes'


class SessionSummary(AbstractGenericModel):
    """ Object to set the Session Summary information for a session."""

    METRIC_PATH = ''
