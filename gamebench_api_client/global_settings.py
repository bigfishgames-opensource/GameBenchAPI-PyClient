""" Global settings for the GameBench API Client."""

GAMEBENCH_CONFIG = {
    'url': 'https://api.production.gamebench.net',
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
