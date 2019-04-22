from gamebench_api_client.api.requests_retriever.builder.url.url_builder import AuthURL, \
    SessionURL


class URLDirector:
    """ Constructs the URL object using the URLBuilder interface."""

    def __init__(self):
        self._builder = None

    def construct_url(self, builder, **request_parameters):
        """ Constructs an URL object.

            :param builder: object which determines which concrete creator to use.
            :param request_parameters: strings used when creating the session URL
                (session_id, metric).
        """

        self._builder = builder
        self._builder.set_suffix(**request_parameters)
        self._builder.set_url()

    @staticmethod
    def get_auth_url():
        """ Constructs an auth URL object and returns the auth
            URL string.

            :return: auth.url - The auth URL string.
        """

        auth = AuthURL()
        director = URLDirector()
        director.construct_url(auth)

        return auth.url

    @staticmethod
    def get_session_url(**request_parameters):
        """ Constructs a session URL object and returns the session
            URL string.

            :param request_parameters: Dictionary from the user containing information
                for the request.
            :return: session.url - The session URL string.
        """

        session = SessionURL()
        director = URLDirector()
        director.construct_url(session, **request_parameters)

        return session.url
