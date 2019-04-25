Using the GameBench API Client
==============================

Installation
------------

The GameBench API Client can be install using pip:

.. code-block:: python

    pip install GameBenchAPI-PyClient-BigFish

It can also be found on the `GitHub`_ page.


Setup
-----

Add the username and password for the GameBench account you are using to the 'global_settings.py'
module.

.. code-block:: python
   :linenos:

    GAMEBENCH_CONFIG = {
        'url': 'https://api.production.gamebench.net',
        'api_version': '/v1',
        'username': 'john.smith@example.com',
        'password': 'password',
        'company_id': '',
    }

See :doc:`global_settings` for for information on this module.


Basic Usage
-----------

In the module that will be calling the API Client, import the ModelCreator class.

.. code-block:: python

    from gamebench_api_client.models.creator.model_creator import ModelCreator

Create an instance of the ModelCreator and pass in the following information:

 - The model that you want, which should be in a CamelCase style.
 - A dictionary that specifies the information you want.

Here is one example for requesting time series data:

.. code-block:: python
   :linenos:

   time_series_request = {
       'session_id': 66d926f47ff5a7a5d853d1058c6305614e1ae6a5
   }

   creator = ModelCreator('Cpu', time_series_request)

This will make the request to the API and store the returned data.  You can call the
*get_model* method for the *ModelCreator* instance to get the results.

See :doc:`examples` for more dictionary examples.

.. _GitHub: https://github.com/bigfishgames/GameBenchAPI-PyClient
