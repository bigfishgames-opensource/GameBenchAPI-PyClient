Global Settings
================

The global_settings.py module is the home to the global variable GAMEBENCH_CONFIG.
This dictionary holds the API endpoint information that the library uses.
It also contains the username and password for the GameBench account you are using,
and the company ID.

.. code-block:: python
   :linenos:
   :caption: global_settings.py

    GAMEBENCH_CONFIG = {
        'url': 'https://production.node.gce.gamebench.net',
        'api_version': '/v1',
        'username': '',
        'password': '',
        'company_id': '',
    }

If the API endpoint ever changes it can be updated in this file.

Currently the company ID must be manually queried for.  Here are steps on retrieving the ID:

1. Request an API authorisation token using the API calls in the `GameBench API Documentation <https://docs.gamebench.net/api/documentation>`__.
2. Copy down the token from the Response.
3. Contact the following API endpoint, replacing the '<auth_token>' with the token from the first step:

.. code-block:: python

   https://production.node.gce.gamebench.net/v1/users/me?jwt=<auth_token>

4. Find the 'company.id' value.
