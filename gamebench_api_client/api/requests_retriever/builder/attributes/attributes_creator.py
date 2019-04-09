class Attributes:
    """ Class that determines the request's attributes - headers, params, data."""

    # TODO Consider refactoring request_parameters to be an instance member.

    def get_headers(self, **request_parameters):
        """ Determines which headers should be used for the request."""

        if "metric" in request_parameters:
            return self._get_session_headers(**request_parameters)

        else:
            return {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            }

    def get_params(self, **request_parameters):
        """ Determines which parameters should be used for the request."""

        return request_parameters["params"]

    def get_data(self, **request_parameters):
        """ Determines which data should be used for the request.
            In the case of auth requests, this is the username and password of the
            GameBench account.

            For Session requests, this will include the auth token and whatever other
            data is relevant to the specific request being made.
        """

        if self._is_auth_request(**request_parameters):
            return {
                'username': request_parameters['username'],
                'password': request_parameters['password']
            }
        else:
            return request_parameters["data"]

    def _get_session_headers(self, **request_parameters):
        """ Determines which type of session request is being created and returns
            the appropriate headers.

            session_id - id for the current session
                metric - specific category of data being requested
                (cpu, gpu, battery, etc.)
                auth_token - authorization token necessary for retrieving
                data.
            :return: Dictionary containing the headers for the session request.
        """

        if request_parameters["metric"] == "":
            return {
                'accept': 'application/json',
                'Authorization': 'JWT ' + request_parameters["auth_token"],
                'Content-Type': 'application/json'
            }
        else:
            return {
                'accept': 'application/json',
                'Authorization': 'JWT ' + request_parameters["auth_token"]
            }

    def _is_auth_request(self, **request_parameters):
        """ Determine if the request parameters contain a 'username' key.

        If the parameters do contain this key it is an auth request.
        """

        return "username" in request_parameters
