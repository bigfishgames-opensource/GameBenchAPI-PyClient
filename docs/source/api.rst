Using the API
=============

1. Install the package with ‘pip install gamebench_api’ or download it from GitHub.

2. Add the username and password you want to use into GAMEBENCH_CONFIG in the ‘global_settings.py’ module.  When requests are made this information will be used to get the authentication token from the API.

3. Import the ModelCreator class into the module that will be used to send requests.

4. Create an instance of the ModelCreator and pass in the following information:

  - Model you are looking for, which should be in a CamelCase style.

  - Dictionary that includes the information you want from the API.  Example dictionaries can be found in the ‘Examples’ section of the documentation.

5. This will build and make the request to the API.

6. Call the get_model method for your ModelCreator instance and your results will be returned.
