class Attributes:
    """ Class that determines the request's attributes - headers, params, data.

        :param request_parameter: Dictionary provided by the user.
    """

    def __init__(self, **request_parameters):

        self.request_parameters = request_parameters

    def get_headers(self):
        """ Determines which headers should be used for the request.

            :return: A dictionary containing the needed Headers for a request.
        """

        if "metric" in self.request_parameters:
            return self._get_session_headers()

        else:
            return {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            }

    def get_params(self):
        """ Determines which parameters should be used for the request.

            :return: A Dictionary containing the needed 'params' key/value pair.
        """

        return self.request_parameters.get('params', '')

    def get_data(self):
        """ Determines which data should be used for the request.

            In the case of auth requests, this is the username and password of the
            GameBench account.  For other requests it will include the information
            provided by the user, or an empty string if nothing was provided.

            :return: A Dictionary containing either the username and password,
                or the data key and its value.
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

            For most session requests, this will include the auth token and the 'accept' key/value pair.
            Requests that don't need a session_id will also include the 'Content-Type'
            key/value pair.

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

            :return: Bool of whether or not there is a 'username' key in the
                request_parameter dictionary.
        """

        return "username" in self.request_parameters
