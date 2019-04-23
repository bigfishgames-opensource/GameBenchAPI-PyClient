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
        'url': 'https://api.production.gamebench.net',
        'api_version': '/v1',
        'username': '',
        'password': '',
        'company_id': '',
    }

If the API endpoint ever changes it can be updated in this file.

The company ID can be found on the `GameBench Web Dashboard <https://web.gamebench.net>`__.
Once signed in go to the 'My Account' section.  The company id is the alpha-numeric string
in the URL.
