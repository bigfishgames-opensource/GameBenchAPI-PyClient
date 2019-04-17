Request Examples
================

In order to make a request the client simply has to import the ModelCreator class.
When the ModelCreator is instantiated it takes two arguments.  The first is a 'model' argument
which should be the name of the metric that you are looking for, and be in a CamelCase style.
This is used by the library to dynamically import the needed model class.  The second argument is
a dictionary which must include specific key/value pairs for the library to retrieve the required information.

Here are examples of the dictionaries that can be passed to the ModelCreator as an argument
to get back information.

Time-Series Model
-----------------
This type of request is used for the following models: Battery, Cpu, CPU Core Frequency,
Energy, FPS, FPS Stability, GPU (Imagination), GPU, Janks, Memory, Network, and Power.

.. code-block:: python
   :linenos:

   time_series_request = {
       'session_id': 66d926f47ff5a7a5d853d1058c6305614e1ae6a5,
       'metric': '/cpu',
       'detail': '',
       'params': '',
       'data': ''
   }

   creator = ModelCreator(time_series_request)


Generic Model
-------------
This type of request is used for the following models: Keyword, Markers, Session Notes,
and Session Summary.

.. code-block:: python
   :linenos:

    generic_request = {
        'session_id': 66d926f47ff5a7a5d853d1058c6305614e1ae6a5,
        'metric': '/notes',
        'detail': '',
        'params': '',
        'data': ''
    }

    creator = ModelCreator(generic_request)


Session Detail Model
--------------------
This type of request is used to get specific metrics from the summary data and includes
the following information: App, Device, Location, Metrics, and Network Usage.

.. code-block:: python
   :linenos:

    session_detail_request = {
        'session_id': 66d926f47ff5a7a5d853d1058c6305614e1ae6a5,
        'metric': '',
        'detail': 'app',
        "params": '',
        "data": ''
    }

    creator = ModelCreator(session_detail_request)
