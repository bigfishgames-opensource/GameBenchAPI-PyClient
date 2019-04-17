Examples
========



When the ModelCreator is called it requires a dictionary to be passed in which contains the
information that the client wants.  It takes a 'model' argument which should be the name of
the metric that you are looking for, and be in a CamelCase style.  Here are examples of the
dictionaries that can be passed to the ModelCreator as an argument to get back information.

Time-Series Model
-----------------
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
.. code-block:: python
   :linenos:

    {
        'session_id': SESSION_ID,
        'metric': '',
        'detail': 'app',
        "params": '',
        "data": ''
    }
