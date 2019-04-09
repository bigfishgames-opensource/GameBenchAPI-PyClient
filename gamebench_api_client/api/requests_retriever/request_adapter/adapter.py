from abc import ABC, abstractmethod


class Adapter(ABC):
    """ Abstract adapter for external HTTP request services."""

    def __init__(self):
        """ Abstract init that creates an empty service object."""

        self._http_library = None

    @abstractmethod
    def request(self):
        """ Abstract method to make a request."""

        pass


class RequestsAdapter(Adapter):
    """ Concrete adapter to use the Requests library to send an api call."""

    def __init__(self, **request_attributes):
        """ Receives request attributes to use for the request and creates _service object.

            The request library is imported within the init to help define exactly where it is used.

            :param request_attributes: Dictionary containing the following keys and values:
                method - Request method to use (POST, GET, etc.).
                url - Rest endpoint to send a request to.
                attributes - Dictionary containing other keyword arguments to add to the request.
        """

        super().__init__()
        import requests
        self._http_library = requests
        self.method = request_attributes["method"]
        self.url = request_attributes["url"]
        self.attributes = request_attributes["attributes"]

    def request(self):
        """ Concrete implementation to send a request call through Requests.

            :return: A requests.Response object - http://docs.python-requests.org/en/master/api/#requests.Response
        """

        return self._http_library.request(self.method, self.url, **self.attributes)
