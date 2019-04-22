from importlib import import_module


class ModelCreator:
    """ Creates model objects based on the users requirements.

        Class variables are composed of the different models and which modules they are in.
    """

    MODELS_AND_MODULES = {
        "gamebench_api_client.models.dataframes.generic.generic_models":
            ["Keyword", "Markers", "SessionNotes", "SessionSummary"],
        "gamebench_api_client.models.dataframes.session_detail.session_detail_models":
            ["App", "Device", "Location", "Metrics", "NetworkUsage"],
        "gamebench_api_client.models.dataframes.time_series.time_series_models":
            [
                "Battery", "Cpu", "CpuCoreFrequency", "Energy", "Fps", "FpsStability",
                "Energy", "GpuImg", "Gpu", "Janks", "Memory", "Network", "Power"
            ]
    }

    def __init__(self, model, **request_parameters):
        """ Sets up the instance of a needed model.

            :param model: The name of the model that the user wants.
            :param request_parameters: This will be a dictionary from the
                client that includes the following keys:

                    session_id: ID for a specific session.
                    metric: Which metric the user requested (cpu, memory, etc.).
                    auth_token: Auth token for the user.
                    params: URL appended filters.
                    data: Dictionary of filter keywords.
        """

        self.model = model
        self.module_path = self._set_module_name_by_model()
        self.imported_module = self._import_given_model_module()
        self.model_class = self._get_class_object()
        self.instance = self.model_class(**request_parameters)

    def _set_module_name_by_model(self):
        """ Determine which module the given model is in and returns the module path.

            :return: The path to the module containing the requested model.
            :raises ValueError: Raised if the model doesn't exist.
        """

        for path, models in self.MODELS_AND_MODULES.items():
            if self.model in models:
                return path
        else:
            raise ModelNotFound(self.model)

    def _import_given_model_module(self):
        """ Use import module that contains the specified class name.

            :return: Imported module name.
        """

        return import_module(self.module_path)

    def _get_class_object(self):
        """ Get the value of the model class.

            :return: Value of the model's class.
        """

        return getattr(self.imported_module, self.model)

    def get_model(self):
        """ Returns the instance of a specified model.

            :return instance: Instance of a model.
        """

        return self.instance


class ModelNotFound(Exception):
    """ Raised when the model given doesn't exist."""

    def __init__(self, model):
        Exception.__init__(self, f"The {model} model does not exist.")
