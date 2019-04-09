""" This module is responsible for getting the Authentication token for the client.

    The Authenticator is an interface to the Mediator which contacts the lower-
    level logic to actually build and send requests.
"""

from gamebench_api_client.api.response.response_mediator import AuthenticationMediator
from gamebench_api_client.models.abstract_model import AbstractModel
from gamebench_api_client.singleton import Singleton


class Authenticator(AbstractModel, Singleton):
    """ Class responsible for obtaining an authentication token."""

    def __init__(self, **request_parameters):
        """ Sets up the mediator and data attributes.

            The mediator is set to the mediator that it will be contacting.  The data
            is the return from the get_token method.

            :param request_parameters: Dictionary containing the client's username and password.
        """

        super().__init__()
        self.mediator = AuthenticationMediator()
        self.data = self.get_data(**request_parameters)
        self.token = self.get_data

    def get_data(self, **request_parameters):
        """ Calls the get_data method from the Mediator object.

            :param request_parameters: Dictionary containing the client's username and password.
            :return: The authentication token as a JSON.
        """

        return self.mediator.get_data(**request_parameters)
