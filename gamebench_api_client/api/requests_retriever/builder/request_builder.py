from abc import ABC, abstractmethod

from gamebench_api_client.api.requests_retriever.builder.attributes.attributes_creator import \
    Attributes
from gamebench_api_client.api.requests_retriever.builder.method.method_creator import Method


class RequestBuilder(ABC):
    """ Abstract interface for building requests."""

    def __init__(self, **request_parameters):
        """ Creates an instance of the Request object for construction.

            :param request_parameters:
                session_id - id for the current session
                metric - specific category of data being requested  (cpu, gpu, battery, etc.)
                auth_token - authorization token necessary for retrieving data.
                params - parameters appended to certain session requests (pageSize, timePushed, etc.)
                data - json body appended to certain session requests
                (example: {"apps" : [], "devices" : [], "manufacturers" : []})
        """

        self.request_parameters = request_parameters
        self.request = Request()
        self.attributes = Attributes(**self.request_parameters)
        self.method = Method(**self.request_parameters)

    @abstractmethod
    def set_method(self):
        """ Set the proper method for each request.

            This can be any valid request method (POST, GET, etc.).
        """

        pass

    @abstractmethod
    def set_url(self, url_director):
        """ Set the correct url for the request.

            This will call the URL Builder methods to build the
            needed URL.
        """

        pass

    @abstractmethod
    def set_headers(self):
        """ Set the correct headers for the request."""

        pass

    @abstractmethod
    def set_params(self):
        """ Set any necessary parameters for the request.

            These are items such as searching for a company ID
            or limiting the number of items returned.
        """

        pass

    @abstractmethod
    def set_data(self):
        """ Set any necessary data to send to the API.

            This is used for authentication requests, or requesting
            specific searches back.
        """

        pass


class AuthRequest(RequestBuilder):
    """ Concrete builder that constructs and assembles the auth request object.

        :param request_parameters: Dictionary containing information needed to build the request.
    """

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)

    def set_method(self):
        """ Implementation of the abstract set_method method.

            Sets the proper method property for authentication
            requests.
        """

        self.request.method = self.method.get_method()

    def set_url(self, url_director):
        """ Implementation of the abstract set_method method.

            Calls the URL Builder methods to build the auth URL and
            sets the url property.
        """

        self.request.url = url_director.get_auth_url()

    def set_headers(self):
        """ Implementation of the abstract set_headers method.

            Sets the proper headers property for authentication
            requests.
        """

        self.request.headers = self.attributes.get_headers()

    def set_params(self):
        """ Implementation of the abstract set_params method.

            Sets the proper params property for authentication
            requests (Note - there aren't any).
        """

        pass

    def set_data(self):
        """ Implementation of the abstract set_data method.

            Sets the data property for authentication requests.
        """

        self.request.data = self.attributes.get_data()


class SessionRequest(RequestBuilder):
    """ Concrete builder that constructs and assembles the session
        request object by implementing the RequestBuilder interface.
    """

    def __init__(self, **request_parameters):
        super().__init__(**request_parameters)

    def set_method(self):
        """ Implementation of the abstract set_method method.

            Sets the proper method property for session requests.
        """

        self.request.method = self.method.get_method()

    def set_url(self, url_director):
        """ Implementation of the abstract set_method method.

            Calls the URL Builder methods to build the session URL
            and sets the url property.
        """

        self.request.url = url_director.get_session_url(**self.request_parameters)

    def set_headers(self):
        """ Implementation of the abstract set_headers method.

            Sets the proper headers property for session
            requests.
        """

        self.request.headers = self.attributes.get_headers()

    def set_params(self):
        """ Implementation of the abstract set_params method.

            Sets the proper params property for session
            requests.
        """

        self.request.params = self.attributes.get_params()

    def set_data(self):
        """ Implementation of the abstract set_data method.

            Sets the proper data property for session
            requests.
        """

        self.request.data = self.attributes.get_data()


class Request(object):
    """ The request object under construction."""

    pass
