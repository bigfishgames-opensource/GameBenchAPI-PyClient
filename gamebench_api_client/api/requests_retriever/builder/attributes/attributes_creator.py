class Attributes:
    """ Class that determines the request's attributes - headers, params, data."""

    def __init__(self, **request_parameters):

        self.request_parameters = request_parameters

    def get_headers(self):
        """ Determines which headers should be used for the request."""

        if "metric" in self.request_parameters:
            return self._get_session_headers()

        else:
            return {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            }

    def get_params(self):
        """ Determines which parameters should be used for the request."""

        return self.request_parameters.get('params', '')

    def get_data(self):
        """ Determines which data should be used for the request.

            In the case of auth requests, this is the username and password of the
            GameBench account.

            For Session requests, this will include the auth token and whatever other
            data is relevant to the specific request being made.
        """

        if self._is_auth_request():
            return {
                'username': self.request_parameters['username'],
                'password': self.request_parameters['password']
            }
        return self.request_parameters.get('data', '')

    def _get_session_headers(self):
        """ Determines which type of session request is being created and returns
            the appropriate headers.

            session_id - id for the current session
                metric - specific category of data being requested
                (cpu, gpu, battery, etc.)
                auth_token - authorization token necessary for retrieving
                data.
            :return: Dictionary containing the headers for the session request.
        """

        if self.request_parameters["session_id"] == '':
            return {
                'accept': 'application/json',
                'Authorization': 'JWT ' + self.request_parameters["auth_token"],
                'Content-Type': 'application/json'
            }
        else:
            return {
                'accept': 'application/json',
                'Authorization': 'JWT ' + self.request_parameters["auth_token"]
            }

    def _is_auth_request(self):
        """ Determine if the request parameters contain a 'username' key.

            If the parameters contain this key it is an auth request.
        """

        return "username" in self.request_parameters
