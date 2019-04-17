""" This module is responsible for getting the Authentication token for the client.

    The Authenticator is an interface to the Mediator which contacts the lower-
    level logic to actually build and send requests.
"""

from gamebench_api_client.api.response.response_mediator import AuthenticationMediator
from gamebench_api_client.global_settings import get_username_and_password
from gamebench_api_client.models.abstract_model import AbstractModel
from gamebench_api_client.singleton import Singleton


class Authenticator(AbstractModel, Singleton):
    """ Class responsible for obtaining an authentication token."""

    def __init__(self):
        """ Sets up the mediator and data attributes.

            The mediator is set to the mediator that it will be contacting.  The data
            is the return from the get_token method.

        """

        super().__init__()
        username_and_password = get_username_and_password()
        self.mediator = AuthenticationMediator(**username_and_password)
        self.data = self.get_data()
        self.token = self.get_data

    def get_data(self):
        """ Calls the get_results method from the Mediator object.

            :return: The authentication token as a JSON.
        """

        return super().get_data()
