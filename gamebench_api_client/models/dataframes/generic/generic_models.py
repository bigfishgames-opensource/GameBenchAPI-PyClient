""" All modules that use the GenericMediator.

    The classes inherit from the AbstractGenericModel.
    Each model is kept as its own class so new behavior can be added
    individually as needed.
"""

from gamebench_api_client.models.dataframes.generic.abstract_generic import AbstractGenericModel


class Keyword(AbstractGenericModel):
    """ Object to set the results for a keyword search."""

    pass


class Markers(AbstractGenericModel):
    """ Object to set the Markers information for a session."""

    pass


class SessionNotes(AbstractGenericModel):
    """ Object to set the Session Notes for a session."""

    pass


class SessionSummary(AbstractGenericModel):
    """ Object to set the Session Summary information for a session."""

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)
        self.app = self.get_data().filter(['app'])

