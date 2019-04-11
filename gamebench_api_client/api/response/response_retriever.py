from abc import ABC, abstractmethod

from gamebench_api_client.api.requests_retriever.builder.request_director import RequestDirector
from gamebench_api_client.api.requests_retriever.request_adapter.adapter import RequestsAdapter


class AbstractRetriever(ABC):
    """ Abstract retriever class for contacting the RequestDirector and RequestAdapter.

        When instantiated a network call will be made through the Request Adapter.

        :param request_parameters: Dictionary from the user containing information
                for the request.
    """

    def __init__(self, **request_parameters):
        self.request_parameters = request_parameters
        self.director = RequestDirector(**self.request_parameters)
        self.request = None
        self.adapter = None
        self.response = None

    @abstractmethod
    def get_response_json(self):
        """ Abstract method to return the JSON of the response object.

            :return: The JSON data for a response.
        """

        return self.response.json()


class ResponseRetriever(AbstractRetriever):
    """ Facade to retrieve data for non-auth requests."""

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)
        self.request = self.director.get_session_request()
        self.adapter = RequestsAdapter(**self.request)
        self.response = self.adapter.request()

    def get_response_json(self):
        """ Return the JSON of the response object.

            :return: The JSON data for a response.
         """

        return super().get_response_json()


class AuthResponseRetriever(AbstractRetriever):
    """ Facade for getting Auth token from the Request.

        :param request_parameters: Dictionary containing information needed for
            an authentication request.  Example:
            {'username': 'John@gmail.com', 'password': '1234'}
    """

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)
        self.request = self.director.get_auth_request()
        self.adapter = RequestsAdapter(**self.request)
        self.response = self.adapter.request()

    def get_response_json(self):
        """ Return the JSON of the response object.

            :return: The JSON data for a response.
        """

        return super().get_response_json()
