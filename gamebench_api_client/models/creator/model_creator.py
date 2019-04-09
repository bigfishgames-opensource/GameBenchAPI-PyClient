from importlib import import_module


class ModelCreator:
    """ Creates model objects based on the users requirements.

        Class variables are composed of the different models and
        which modules they are in.
    """

    MODELS_AND_MODULES = {
        "gamebench_api_client.models.generic.generic_frame_models":
            ["Keyword", "Markers", "SessionNotes", "SessionSummary"],
        "gamebench_api_client.models.session_detail.session_detail_models":
            ["App", "Device", "Location", "Metrics", "NetworkUsage"],
        "gamebench_api_client.models.time_series.time_series_models":
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
                    method: POST, GET, etc.
                    session_id: ID for a specific session.
                    metric: Which metric the user requested (cpu, memory, etc.).
                    auth_token: Auth token for the user.
                    params: URL appended filters.
                    data: Dictionary of filter keywords.
        """
        # TODO set self.model = model
        self.module_path = self._find_module_containing_model(model)
        # TODO Add set_module_path(module_path) if given a path, use it, if not _find_module_path()
        self.imported_module = self._import_given_model_module(self.module_path)
        self.model_class = self._get_class_object(self.imported_module, model)
        self.instance = self.model_class(**request_parameters)

    def _find_module_containing_model(self, model):
        """ Determine which module the given model is in and returns the module path.

            :param model: The model that the client is requesting.
            :return: The path to the module containing the requested model.
            :raises ValueError: Raised if the model doesn't exist.
        """

        for path, models in self.MODELS_AND_MODULES.items():
            if model in models:
                return path
        else:
            raise ModelNotFound(model)

    def _import_given_model_module(self, module_path):
        """ Use import module that contains the specified class name.

            :param module_path: The path to the module containing the required model.
            :return: Imported module name.
        """
        # TODO Refactor to import_module(self.module_path) since this happens after self.module_path is set.
        return import_module(module_path)

    def _get_class_object(self, imported_module, class_name):
        """ Get the value of the model class.

            :param imported_module: The module containing the model the user requested.
            :param class_name: The class name for the model the user requested.
            :return: Value of the model's class.
        """
        # TODO refactor to use instance members.
        return getattr(imported_module, class_name)

    def get_model(self):
        """ Returns the instance of a specified model.

            :return instance: Instance of a model.
        """

        return self.instance


class ModelNotFound(Exception):
    """ Raised when the model given doesn't exist."""

    def __init__(self, model):
        Exception.__init__(self, f"The {model} model does not exist.")
