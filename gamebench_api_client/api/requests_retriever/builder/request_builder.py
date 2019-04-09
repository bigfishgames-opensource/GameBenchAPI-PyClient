from abc import ABC, abstractmethod

from gamebench_api_client.api.requests_retriever.builder.attributes.attributes_creator import \
    Attributes
from gamebench_api_client.api.requests_retriever.builder.method.method_creator import Method


class RequestBuilder(ABC):
    """ Abstract interface for building requests."""

    def __init__(self):
        """ Creates an instance of the Request object for
            construction.
        """

        self.request = Request()
        self.attributes = Attributes()
        self.method = Method()

    @abstractmethod
    def set_method(self):
        """ Set the proper method for each request.

            This can be any valid request method (POST, GET, etc.).
        """

        pass

    @abstractmethod
    def set_url(self, url_director, **request_parameters):
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
    """ Concrete builder that constructs and assembles the auth
        request object by implementing the RequestBuilder interface.
    """

    def set_method(self, **request_parameters):
        """ Implementation of the abstract set_method method.

            Sets the proper method property for authentication
            requests.
        """

        self.request.method = self.method.get_method(**request_parameters)

    def set_url(self, url_director, **request_parameters):
        """ Implementation of the abstract set_method method.

            Calls the URL Builder methods to build the auth URL and
            sets the url property.
        """

        self.request.url = url_director.get_auth_url()

    def set_headers(self, **request_parameters):
        """ Implementation of the abstract set_headers method.

            Sets the proper headers property for authentication
            requests.
        """

        self.request.headers = self.attributes.get_headers(**request_parameters)

    def set_params(self, **request_parameters):
        """ Implementation of the abstract set_params method.

            Sets the proper params property for authentication
            requests (Note - there aren't any).
        """

        pass

    def set_data(self, **request_parameters):
        """ Implementation of the abstract set_data method.

            Sets the data property for authentication requests.
        """

        self.request.data = self.attributes.get_data(**request_parameters)


class SessionRequest(RequestBuilder):
    """ Concrete builder that constructs and assembles the session
        request object by implementing the RequestBuilder interface.
    """

    def set_method(self, **request_parameters):
        """ Implementation of the abstract set_method method.

            Sets the proper method property for session requests.
        """

        self.request.method = self.method.get_method(**request_parameters)

    def set_url(self, url_director, **request_parameters):
        """ Implementation of the abstract set_method method.

            Calls the URL Builder methods to build the session URL
            and sets the url property.
        """

        self.request.url = url_director.get_session_url(**request_parameters)

    def set_headers(self, **request_parameters):
        """ Implementation of the abstract set_headers method.

            Sets the proper headers property for session
            requests.
        """

        self.request.headers = self.attributes.get_headers(**request_parameters)

    def set_params(self, **request_parameters):
        """ Implementation of the abstract set_params method.

            Sets the proper params property for session
            requests.
        """

        self.request.params = self.attributes.get_params(**request_parameters)

    def set_data(self, **request_parameters):
        """ Implementation of the abstract set_data method.

            Sets the proper data property for session
            requests.
        """

        self.request.data = self.attributes.get_data(**request_parameters)


class Request(object):
    """ The request object under construction."""

    pass
