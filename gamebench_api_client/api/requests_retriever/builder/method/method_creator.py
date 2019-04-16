class Method:
    """ Class that determines the request method."""

    def __init__(self, **request_parameters):
        """ Create the instance variable for given dictionary.

        :param request_parameters: Dictionary containing information needed to set the method.
        """

        self.request_parameters = request_parameters

    def get_method(self):
        """ Determines request method.

        If there is a metric (gpu, cpu, battery, etc.) the request will
        be set as "GET", otherwise it is a "POST".
        """

        if self.is_metric_present():
            return "POST"
        else:
            return "GET"

    def is_metric_present(self):
        """ Determine if there is a metric present in the request parameters."""

        return 'session_id' not in self.request_parameters or self.request_parameters['session_id'] == ''
