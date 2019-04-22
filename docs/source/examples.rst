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
       'session_id': 66d926f47ff5a7a5d853d1058c6305614e1ae6a5
   }

   creator = ModelCreator('Cpu', time_series_request)

Here is how you can get the DataFrame from your request and what it looks like:

.. code-block:: python
   :linenos:

   model = creator.get_model()
   print(model.data)

         appUsage  daemonUsage    gbUsage  timestamp  totalCpuUsage
   0  1372571.375            0  12.658228       5257      39.688461


When requesting time-series data, simply pass in the model you want as the first argument
to the ModelCreator.  The given dictionary then just needs to include the 'session_id' key
and the associated id as the value.

Generic models
--------------
This type of request is used for the following models: Keyword, Markers, Session Notes,
and Session Summary.

.. code-block:: python
   :linenos:

    generic_request = {
        'session_id': 66d926f47ff5a7a5d853d1058c6305614e1ae6a5
    }

    creator = ModelCreator('SessionNotes', generic_request)



When requesting the session summary, markers, or notes for a session, the given dictionary only needs to include
the session id.  However, there are two other requests that can be made.

Keyword Search
^^^^^^^^^^^^^^
This type of request allows you to pass in keywords that can be used to search for specific
sessions.  Adding a 'data' dictionary to the given dictionary will allow you to give keywords
to search for.

**Example:**

.. code-block:: python
   :linenos:

   generic_request = {
        'data': {
            'query': 'iPad'
        }
   }

Sessions
^^^^^^^^
This type of request is different from the session summary request as it gives the summary information
for multiple sessions.  by passing in the appropriate key/value pairs, you can search for available
sessions through the GameBench API.

Adding a 'params' key to the given dictionary will allow you to give search parameters.

**Example:**

.. code-block:: python
   :linenos:

   generic_request = {
        'params': {
            'pageSize': 15
        }
   }


To see a full list of the available search options, see the
`GameBench API Documentation <https://docs.gamebench.net/api/documentation>`__.
