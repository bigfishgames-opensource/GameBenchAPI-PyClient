"""" Director interface for getting requests from the builder."""

from gamebench_api_client.api.requests_retriever.builder.request_builder import AuthRequest, \
    SessionRequest
from gamebench_api_client.api.requests_retriever.builder.url.url_director import \
    URLDirector


class RequestDirector:
    """ Constructs the Request object using the RequestBuilder interface."""

    # TODO consider refactoring request_parameters to be an instance member.

    def __init__(self):
        """ Set up the _builder to be used by the constructor."""

        self._builder = None
        self._loader = DirectorLoader()
        self._url_director = None

    def construct_request(self, builder, **request_parameters):
        """ Constructs a Request objects.

            :param builder: object which determines which concrete creator
            to use.
            :param request_parameters: dictionary used for adding necessary
            data to the set methods.
        """

        self._url_director = self._loader.set_url_director()
        self._builder = builder

        self._builder.set_method(**request_parameters)
        self._builder.set_url(self._url_director, **request_parameters)
        self._builder.set_headers(**request_parameters)
        self._builder.set_params(**request_parameters)
        self._builder.set_data(**request_parameters)

    def get_auth_request(self, **request_parameters):
        """ Constructs an authorization request object and returns the properties
            as a dictionary.

            :param request_parameters: User credentials required for generating an
            auth token:
                username - GameBench account username.
                password - GameBench account password.
            :return: request - dictionary containing each element of the auth request.
        """

        auth = AuthRequest()
        director = RequestDirector()
        director.construct_request(auth, **request_parameters)

        request = self._auth_to_dict(auth)

        return request

    def _auth_to_dict(self, auth_object):
        """ Helper method to turn the auth object into a dictionary to return it.

            :param auth_object: authorization object.
            :return auth_request: dictionary containing the attributes of the authorization
            object.
        """
        # TODO consider making this a static method unless there is an instance member hiding here.
        auth_request = {
            'method': auth_object.request.method,
            'url': auth_object.request.url,
            'attributes': {
                'headers': auth_object.request.headers,
                'auth': (
                    auth_object.request.data['username'],
                    auth_object.request.data['password']
                )
            }
        }

        return auth_request

    def get_session_request(self, **request_parameters):
        """ Constructs and returns a session request object.

            :param request_parameters:
                session_id - id for the current session
                metric - specific category of data being requested
                (cpu, gpu, battery, etc.)
                auth_token - authorization token necessary for retrieving
                data.
                params - parameters appended to certain session requests
                (pageSize, timePushed, etc.)
                data - json body appended to certain session requests
                (example: {"apps" : [], "devices" : [], "manufacturers" : []})
            :return: request - dictionary containing each element of the
            session request.
        """

        session = SessionRequest()
        director = RequestDirector()
        director.construct_request(session, **request_parameters)

        request = self._session_to_dict(session)

        return request

    def _session_to_dict(self, session_object):
        """ Helper method to turn the session object into a dictionary.

            :param session_object: session request object.
            :return session_request: dictionary containing the attributes of the
            session object.
        """

        # TODO consider making this a static method unless there is an instance member hiding here.
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
