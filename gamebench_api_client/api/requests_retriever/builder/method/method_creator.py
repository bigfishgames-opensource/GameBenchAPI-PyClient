class Method:
    """ Class that determines the request method."""

    # TODO consider making request_parameters an instance member.

    def get_method(self, **request_parameters):
        """ Determines request method.

        If there is a metric (gpu, cpu, battery, etc.) the request will
        be set as "GET", otherwise it is a "POST".
        """

        if self.is_metric_present(**request_parameters):
            return "POST"
        else:
            return "GET"

    def is_metric_present(self, **request_parameters):
        """ Determine if there is a metric present in the request parameters."""

        return "metric" not in request_parameters or request_parameters["metric"] == ""
