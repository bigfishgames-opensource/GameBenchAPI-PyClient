""" Global settings for the GameBench API Client."""

GAMEBENCH_CONFIG = {
    'url': 'https://production.node.gce.gamebench.net',
    'api_version': '/v1',
    'username': '',
    'password': '',
    'company_id': '',
}


def set_api_endpoint():
    """ Concatenates the url and api_version to return the full api endpoint.

        :return api_endpoint: concatenated string of the url and the api_version
            from the GAMEBENCH_CONFIG dictionary.
    """

    api_endpoint = GAMEBENCH_CONFIG['url'] + GAMEBENCH_CONFIG['api_version']
    return api_endpoint


def get_username_and_password():
    """ Takes the username and password from global variable GAMEBENCH_CONFIG and returns it as a dictionary.

    :return: user_credentials: Dictionary of key username and value password from the global variable GAMEBENCH_CONFIG
    """

    user_credentials = dict()
    user_credentials['username'] = GAMEBENCH_CONFIG['username']
    user_credentials['password'] = GAMEBENCH_CONFIG['password']
    return user_credentials
