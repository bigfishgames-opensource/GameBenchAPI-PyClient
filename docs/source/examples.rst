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

    from gamebench_api_client.models.creator.model_creator import ModelCreator


   time_series_request = {
       'session_id': '66d926f47ff5a7a5d853d1058c6305614e1ae6a5'
   }

   creator = ModelCreator('Cpu', time_series_request)
   cpu_time_series = creator.get_model()

   results = cpu_time_series.data

   print(results)

   """
         appUsage  daemonUsage    gbUsage  timestamp  totalCpuUsage
   0  1372571.375            0  12.658228       5257      39.688461
   """

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
        'session_id': '66d926f47ff5a7a5d853d1058c6305614e1ae6a5'
    }

    creator = ModelCreator('SessionNotes', generic_request)



When requesting the session summary, markers, or notes for a session, the given dictionary only needs to include
the session id.  However, there are two other requests that can be made.


Keyword Search
^^^^^^^^^^^^^^
This type of request allows you to pass in keywords in order to get a return an array of keyword objects based on the
query..  Adding a 'data' dictionary to the given dictionary will allow you to give keywords to search for.

The following example will search for sessions that contain the parameter 'iPad'.

**Example:**

.. code-block:: python
   :linenos:

   generic_request = {
        'data': '{
            "query": "Google"
        }'
   }

   creator = ModelCreator('Keyword', generic_request)

*NOTE:* When using the 'data' key the value must be a string with the outer quotes as single-quotes, and any inner
quotes as double-quotes.

The response is an array of dictionaries.

**Example**

.. code-block:: python
   :linenos:

   [
      {'key': 'Google', 'doc_count': 3804, 'type': 'manufacturer'},
      {'key': 'Google', 'doc_count': 27, 'type': 'app'},
      {'key': 'Google Pixelbook', 'doc_count': 9, 'type': 'device'}
   ]


App, Device, or Manufacturer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The API allows filtering by three different keywords: apps, device, and manufacturer.  The 'key' values from the
query search can be used as keywords in this search.  This request will return sessions recorded that match the
specified keywords.

**Example**

.. code-block:: python
   :linenos:

   generic_request = {
        'data': '{
            "apps": ["Google"]
        }'
   }

You can use any of these three individually or together.

**Example**

.. code-block:: python
   :linenos:

   generic_request = {
        'data': '{
            "apps": ["Google"],
            "device": ["Google Pixelbook"],
            "manufacturer": ["Google"]
        }'
   }

This will return sessions recorded by the authenticated user.  If you are part of a company, you can include the
'company_id' to expand the search to all sessions from the entire company.  An example of using a 'company_id' can
be seen in the next section.


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
            'company_id': 'QcBvM2IB0D53NS9vlGcH',
            'pageSize': 15
        }
   }

   creator = ModelCreator('SessionSummary', generic_request)

The 'params' value could also be set to a string of exactly what the client wants added as a parameter to the endpoint.

**Example**

.. code-block:: python
   :linenos:

   generic_request = {
      'params': 'company=QcBvM2IB0D53NS9vlGcH&pageSize=15'
   }

   creator = ModelCreator('SessionSummary', generic_request)

This string will be passed to the endpoint to specify the type of response generated.  Either of these two ways will
return the same information.



Session Detail
^^^^^^^^^^^^^^
The session summary information also contains inner dictionaries, such as device information
and app information.  The *SessionSummary* class has class members which let you get just these
details if needed.  For example, if you just wanted information on the device that was used
for testing just call the *SessionSummary.device* variable.  This will return the device
information in a DataFrame.

Here are all of the detail metrics you can call this way: app, device, location, metrics, and
network app usage.


To see a full list of the available search options, see the
`GameBench API Documentation <https://docs.gamebench.net/api/documentation>`__.
