"""" Director interface for getting requests from the builder."""

from gamebench_api_client.api.requests_retriever.builder.request_builder import AuthRequest, \
    SessionRequest
from gamebench_api_client.api.requests_retriever.builder.url.url_director import \
    URLDirector


class RequestDirector:
    """ Constructs the Request object using the RequestBuilder interface."""

    def __init__(self, **request_parameters):
        """ Set up the _builder to be used by the constructor.

            :param request_parameters: Dictionary containing information needed to build the request.
        """

        self.request_parameters = request_parameters
        self._builder = None
        self._loader = DirectorLoader()
        self._url_director = None

    def construct_request(self, builder):
        """ Constructs a Request objects.

            :param builder: object which determines which concrete creator to use.
        """

        self._url_director = self._loader.set_url_director()
        self._builder = builder

        self._builder.set_method()
        self._builder.set_url(self._url_director)
        self._builder.set_headers()
        self._builder.set_params()
        self._builder.set_data()

    def get_auth_request(self):
        """ Constructs an authorization request object and returns the properties
            as a dictionary.

            :return: request - dictionary containing each element of the auth request.
        """

        auth = AuthRequest(**self.request_parameters)
        director = RequestDirector(**self.request_parameters)
        director.construct_request(auth)

        request = self._auth_to_dict(auth)
        return request

    @staticmethod
    def _auth_to_dict(auth_object):
        """ Helper method to turn the auth object into a dictionary to return it.

            :param auth_object: authorization object.
            :return auth_request: dictionary containing the attributes of the authorization
            object.
        """

        auth_request = {
            'method': auth_object.request.method,
            'url': auth_object.request.url,
            'attributes': {
                'headers': auth_object.request.headers,
                'data': {
                    'username': auth_object.request.data['username'],
                    'password': auth_object.request.data['password']
                }
            }
        }

        return auth_request

    def get_session_request(self):
        """ Constructs and returns a session request object.

            :return: request - dictionary containing each element of the session request.
        """

        session = SessionRequest(**self.request_parameters)
        director = RequestDirector(**self.request_parameters)
        director.construct_request(session)

        request = self._session_to_dict(session)

        return request

    @staticmethod
    def _session_to_dict(session_object):
        """ Helper method to turn the session object into a dictionary.

            :param session_object: session request object.
            :return session_request: dictionary containing the attributes of the
            session object.
        """

        session_request = {
            'method': session_object.request.method,
            'url': session_object.request.url,
            'attributes': {
                'headers': session_object.request.headers,
                'params': session_object.request.params,
                'data': session_object.request.data
            }
        }

        return session_request


class DirectorLoader:

    def set_url_director(self):
        _url_director = URLDirector()

        return _url_director
