from abc import ABC, abstractmethod


class AbstractModel(ABC):
    """ Abstract model class.

        The METRIC_PATH class member is created for the individual models
        to add the needed string.
    """

    METRIC_PATH = ''

    def __init__(self, **request_parameters):
        """ Sets up the mediator and data attributes."""

        self.mediator = None
        self.data = None

    @abstractmethod
    def get_data(self):
        """ Returns a Pandas DataFrame containing metric data from a response json.

            :return: Pandas DataFrame containing metric data.
        """

        return self.mediator.get_results()
