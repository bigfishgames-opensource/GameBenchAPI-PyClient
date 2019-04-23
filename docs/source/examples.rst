Request Examples
================

To make a request, import the *ModelCreator* class.
Instantiating the *ModelCreator* requires two arguments.  The first is a CamelCase style 'model'
named after the metric that you are looking for; the model is dynamically imported based on this
name.  The second argument is a dictionary that must include specific key/value pairs for
querying the GameBench API.

Here are examples of the dictionaries that can be passed to the *ModelCreator* as an argument
to get back information.

Time-Series Model
-----------------
This type of request is used for the following models: Battery, Cpu, CPU Core Frequency,
Energy, FPS, FPS Stability, GPU (Imagination), GPU, Janks, Memory, Network, and Power.
Here is an example of how you could get the CPU data for a session and what the DataFrame
for that information looks like:

.. code-block:: python
   :linenos:

   time_series_request = {
       'session_id': "66d926f47ff5a7a5d853d1058c6305614e1ae6a5"
   }

   creator = ModelCreator('Cpu', time_series_request)
   cpu_time_series = creator.get_model()

   print(model.data)

         appUsage  daemonUsage    gbUsage  timestamp  totalCpuUsage
   0  1372571.375            0  12.658228       5257      39.688461


When requesting time-series data, pass in the model you want as the first argument
to the ModelCreator.  The given dictionary then just needs to include the 'session_id' key
and the associated id as the value.

Generic models
--------------
This type of request is used for the following models: Keyword, Markers, Session Notes,
and Session Summary.

.. code-block:: python
   :linenos:

    generic_request = {
        'session_id': "66d926f47ff5a7a5d853d1058c6305614e1ae6a5"
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

   creator = ModelCreator('Keyword', generic_request)

Sessions
^^^^^^^^
This type of request is different from the session summary request as it gives the summary information
for multiple sessions.  by passing in the appropriate key/value pairs, you can search for available
sessions through the GameBench API.  This type of request requires the 'session_id' key, that is
used in normal session summary requests, to either not be included or have an empty string as a
value.

Adding a 'params' key to the given dictionary will allow you to give search parameters.

**Example:**

.. code-block:: python
   :linenos:

   generic_request = {
        'params': {
            'pageSize': 15
        }
   }

   creator = ModelCreator('SessionSummary', generic_request)


To see a full list of the available search options, see the
`GameBench API Documentation <https://docs.gamebench.net/api/documentation>`__.

Session Detail
^^^^^^^^^^^^^^
The session summary information also contains inner dictionaries, such as device information
and app information.  The *SessionSummary* class has class members which let you get just these
details if needed.  For example, if you just wanted information on the device that was used
for testing just call the *SessionSummary.device* variable.  This will return the device
information in a DataFrame.

Here are all of the detail metrics you can call this way: app, device, location, metrics, and
network app usage.
