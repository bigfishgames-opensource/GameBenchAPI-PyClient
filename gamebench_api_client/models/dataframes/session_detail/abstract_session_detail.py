from abc import ABC

from gamebench_api_client.api.response.response_mediator import SessionDetailMediator
from gamebench_api_client.models.abstract_model import AbstractModel


class AbstractSessionDetailModel(AbstractModel, ABC):
    """ Concrete class for models needing to access the Session Detail Mediator.

        Each model is kept as it's own class so new methods can be added
        individually as needed.
    """

    def __init__(self, **request_parameters):
        """ Sets up the mediator and data attributes.

            The mediator is set to the mediator that it will be contacting.  The data
            is set to the DataFrame returned from the get_results method.

            :param request_parameters: Dictionary passed in from the model Creator.  Contains information to
                build and send a response.
        """

        super().__init__()
        self.mediator = SessionDetailMediator(**request_parameters)
        self.data = self.get_data()

    def get_data(self):
        """ Returns a Pandas DataFrame containing metric data from a response json.

            :return: Pandas DataFrame containing metric data.
        """

        return super().get_data()
