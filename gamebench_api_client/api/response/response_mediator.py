from abc import ABC

from gamebench_api_client.api.requests_retriever.builder.request_director import RequestDirector
from gamebench_api_client.api.requests_retriever.request_adapter.adapter import RequestsAdapter
from gamebench_api_client.api.utilities.dataframe_utilities import json_to_normalized_dataframe, \
    session_detail_to_dataframe, to_dataframe


class ResponseMediator(ABC):
    """ Abstract Mediator."""

    def __init__(self):
        self.retriever = None

    def get_data(self, **request_parameters):
        """ Abstract method to get JSON Data into a Pandas DataFrame.

            :param request_parameters: Dictionary from the user containing information
                for the request.
        """

        pass


class TimeSeriesMediator(ResponseMediator):
    """ Concrete Mediator for Time Series objects to use."""

    def __init__(self):
        super().__init__()
        self.retriever = ResponseRetriever()

    def get_data(self, **request_parameters):
        """ Sets JSON data into a Pandas DataFrame.

            :param request_parameters: Dictionary from the user containing information
                for the request.
            :return: DataFrame of the JSON data from a response.
        """

        response_json = self.retriever.get_response_json(**request_parameters)

        return json_to_normalized_dataframe(response_json)


class SessionDetailMediator(ResponseMediator):
    """ Concrete Mediator for session detail objects to use."""

    def __init__(self):
        super().__init__()
        self.retriever = ResponseRetriever()

    def get_data(self, **request_parameters):
        """ Sets JSON data into a Pandas DataFrame.

            :param request_parameters: Dictionary from the user containing information
                for the request.
            :return: DataFrame of the JSON data from a response.
        """

        response_json = self.retriever.get_response_json(**request_parameters['response'])
        session_dict = {
            'metric': request_parameters['metric'],
            'response_json': response_json
        }

        return session_detail_to_dataframe(**session_dict)


class GenericMediator(ResponseMediator):
    """ Concrete Mediator for generic objects to use."""

    def __init__(self):
        super().__init__()
        self.retriever = ResponseRetriever()

    def get_data(self, **request_parameters):
        """ Sets JSON data into a Pandas DataFrame.

            :param request_parameters: Dictionary from the user containing information
                for the request.
            :return: DataFrame of the JSON data from a response.
        """

        response_json = self.retriever.get_response_json(**request_parameters)

        return to_dataframe(response_json)


class ResponseRetriever:
    """ Facade for RequestDirector and RequestsAdapter."""

    def __init__(self):
        self.director = RequestDirector()
        self.request = None
        self.adapter = None
        self.response = None

    def get_response_json(self, **request_parameters):
        """ Retrieves request and returns the JSON.

            :param request_parameters: Dictionary from the user containing information
                for the request.
            :return: The json data for a response.
        """

        self.request = self.director.get_session_request(**request_parameters)
        self.adapter = RequestsAdapter(**self.request)
        self.response = self.adapter.request()

        return self.response.json()


class AuthenticationMediator(ResponseMediator):
    """ Concrete Mediator for Authentication requests to use."""

    def __init__(self):
        super().__init__()
        self.retriever = AuthResponseRetriever()

    def get_data(self, **request_parameters):
        """ Retrieves the Authentication token for a user.

            :param request_parameters: Dictionary from the user containing information
                for the request.
            :return response_json: Auth Token as a JSON.
        """

        response_json = self.retriever.get_response_json(**request_parameters)

        return response_json


class AuthResponseRetriever:
    """ Facade for getting Auth token from the Request."""

    def __init__(self):
        self.director = RequestDirector()
        self.request = None
        self.adapter = None
        self.response = None

    def get_response_json(self, **request_parameters):
        """ Retrieves request and returns the JSON.

            :param request_parameters: Dictionary from the user containing information
                for the request.
            :return: The json data for a response.
        """

        self.request = self.director.get_auth_request(**request_parameters)
        self.adapter = RequestsAdapter(**self.request)
        self.response = self.adapter.request()

        return self.response.json()
