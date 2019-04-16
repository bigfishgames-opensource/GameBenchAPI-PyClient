from abc import ABC

from gamebench_api_client.api.response.response_retriever import AuthResponseRetriever, \
    ResponseRetriever
from gamebench_api_client.api.utilities.dataframe_utilities import json_to_normalized_dataframe, \
    session_detail_to_dataframe, to_dataframe


class ResponseMediator(ABC):
    """ Abstract Mediator.

        :param request_parameters: Dictionary from the user containing information
            for the request.
    """

    def __init__(self, **request_parameters):
        self.request_parameters = request_parameters
        self.retriever = None

    def get_results(self):
        """ Abstract method to get the JSON from the retriever.

            For the Time Series, Generic, and Session Detail mediators this information
            will be returned in a Pandas DataFrame.  The Authentication simply returns
            the Auth Token.
        """

        pass


class TimeSeriesMediator(ResponseMediator):
    """ Concrete Mediator for Time Series objects to use."""

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)
        self.retriever = ResponseRetriever(**self.request_parameters)

    def get_results(self):
        """ Sets JSON data into a Pandas DataFrame.

            :return: DataFrame of the JSON data from a response.
        """

        response_json = self.retriever.get_response_json()

        return json_to_normalized_dataframe(response_json)


class SessionDetailMediator(ResponseMediator):
    """ Concrete Mediator for session detail objects to use."""

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)
        self.retriever = ResponseRetriever(**self.request_parameters)

    def get_results(self):
        """ Sets JSON data into a Pandas DataFrame.

            :return: DataFrame of the JSON data from a response.
        """

        response_json = self.retriever.get_response_json()
        session_dict = {
            'metric': self.request_parameters['detail'],
            'response_json': response_json
        }

        return session_detail_to_dataframe(**session_dict)


class GenericMediator(ResponseMediator):
    """ Concrete Mediator for generic objects to use."""

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)
        self.retriever = ResponseRetriever(**self.request_parameters)

    def get_results(self):
        """ Sets JSON data into a Pandas DataFrame.

            :return: DataFrame of the JSON data from a response.
        """

        response_json = self.retriever.get_response_json()

        return to_dataframe([response_json])


class AuthenticationMediator(ResponseMediator):
    """ Concrete Mediator for Authentication requests to use.

        :param request_parameters:
    """

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)
        self.retriever = AuthResponseRetriever(**self.request_parameters)

    def get_results(self):
        """ Retrieves the Authentication token for a user.

            :return response_json: Auth Token as a JSON.
        """

        response_json = self.retriever.get_response_json()

        return response_json
