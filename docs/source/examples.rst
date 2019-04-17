Examples
========



When the ModelCreator is called it requires a dictionary to be passed in which contains the
information that the client wants.  It takes a 'model' argument which should be the name of
the metric that you are looking for, and be in a CamelCase style.  Here are examples of the
dictionaries that can be passed to the ModelCreator as an argument to get back information.

Time-Series Model
-----------------
This type of request is used for the following models: Battery, Cpu, CPU Core Frequency,
Energy, FPS, FPS Stability, GPU (Imagination), GPU, Janks, Memory, Netowrk, and Power.

.. code-block:: python
   :linenos:

    {
        'session_id': 66d926f47ff5a7a5d853d1058c6305614e1ae6a5,
        'metric': '/cpu',
        'detail': '',
        'params': '',
        'data': ''
    }

Generic Model
-------------
This type of request is used for the following models: Keyword, Markers, Session Notes,
and Session Summary.

.. code-block:: python
   :linenos:

    {
        'session_id': 66d926f47ff5a7a5d853d1058c6305614e1ae6a5,
        'metric': '/notes',
        'detail': '',
        'params': '',
        'data': ''
    }

Session Detail Model
--------------------
This type of request is used to get specific metrics from the summary data and includes 
the following information: App, Device, Location, Metrics, and Network Usage.

.. code-block:: python
   :linenos:

    {
        'session_id': SESSION_ID,
        'metric': '',
        'detail': 'app',
        "params": '',
        "data": ''
    }
