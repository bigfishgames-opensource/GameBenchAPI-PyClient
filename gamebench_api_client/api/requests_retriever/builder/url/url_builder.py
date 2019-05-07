from abc import ABC, abstractmethod

from gamebench_api_client.global_settings import GAMEBENCH_CONFIG


class URLBuilder(ABC):
    """ Abstract interface for creating each part of the URL object."""

    def __init__(self):

        self.url = URL()
        self.base_url = self.url.base_url
        self.version = self.url.version
        self.suffix = None

    @abstractmethod
    def set_suffix(self):
        """ Abstract method for setting the suffix properties to the URL."""

        pass

    @abstractmethod
    def set_url(self):
        """ Base class for setting the completed URL to the URL object."""

        pass


class AuthURL(URLBuilder):
    """ Concrete builder that constructs and assembles the auth URL
        object by implementing UrlBuilder interface.
    """

    def set_suffix(self):
        """ Implementation of the abstract set_suffix method.

            Sets the proper suffix for authentication.
        """

        self.suffix = '/Auth/login'

    def set_url(self):
        """ Implementation of the abstract set_url method.

            Sets the url property to the URL string created by _build_url
        """

        self.url = self._build_url()

    def _build_url(self):
        """ Helper method to concatenate the URL elements into a single
            variable.

            :return: String containing the complete URL.
        """

        return self.base_url + self.version + self.suffix


class SessionURL(URLBuilder):
    """ Concrete builder that constructs and assembles the session URL
        object by implementing UrlBuilder interface.
    """

    def set_suffix(self, **request_parameters):
        """ Implementation of the abstract set_suffix method.

            Creates the suffix variable for the URL object and sets it to the proper suffix for authentication.

            :param request_parameters: session_id, metric - strings representing the session_id and metric respectively.
        """

        self.suffix = '/sessions'
        self._set_session_id(request_parameters["session_id"])
        self._set_metric(request_parameters["metric"])

    def set_url(self):
        """ Implementation of the abstract set_url method.
            Sets the completed URL string to the URL object.
        """
        self.url = self._build_url()

    def _set_session_id(self, session_id):
        """ Helper method to set the session_id.

            If the session_id contains an id it will set the self.session_id variable
            to the given id and a '/' in front of it.  The forward slash is necessary
            for when the id is added onto the end of a URL.

            :param session_id: The session_id for a request.
        """

        if session_id:
            self.session_id = '/' + session_id
        else:
            self.session_id = session_id

    def _set_metric(self, metric):
        """ Helper method to set the session metric. """

        self.metric = metric

    def _build_url(self):
        """ Helper method to concatenate the URL elements into a single
            variable.

            :return: String containing the complete URL.
        """
        return self.base_url + self.version + self.suffix + self.session_id + self.metric


class URL(object):
    """ URL object with basic properties used by the URLBuilder."""

    def __init__(self):
        self.base_url = GAMEBENCH_CONFIG['url']
        self.version = GAMEBENCH_CONFIG['api_version']
