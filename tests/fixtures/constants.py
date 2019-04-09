# Universal
BASE_URL = 'https://api.production.gamebench.net'
VERSION = '/v1'
API_SAMPLES = '/tests/fixtures/API_SAMPLES/'

# Authentication Related
USERNAME = 'john.smith@example.com'
PASSWORD = 'password'
AUTH_SUFFIX = '/Auth/login'
AUTH_URL = BASE_URL + VERSION + AUTH_SUFFIX
AUTH_TOKEN = "test_token"
AUTH_RESPONSE = {
    'token': 'test_token'
}
AUTH_HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
AUTH_DATA = {
    'username': USERNAME,
    'password': PASSWORD
}
AUTH_ATTRIBUTES = {
    'method': 'POST',
    'url': AUTH_URL,
    'attributes': {
        'headers': AUTH_HEADERS,
        'auth': (USERNAME, PASSWORD),
    }
}

# Session Related
SESSION_SUFFIX = '/sessions'
SESSION_ID = "/session_id"
METRIC = "/cpu"
DEFAULT_SESSION_URL = BASE_URL + VERSION + SESSION_SUFFIX + SESSION_ID + METRIC
SESSION_DATA = {
    "data": {
        "test_data": "test_data"
    }
}
DEFAULT_SESSION_HEADERS = {
    'accept': 'application/json',
    'Authorization': 'JWT ' + AUTH_TOKEN
}
NO_METRIC_HEADERS = {
    'accept': 'application/json',
    'Authorization': 'JWT ' + AUTH_TOKEN,
    'Content-Type': 'application/json'
}
SESSION_ATTRIBUTES = {
    'method': 'GET',
    'url': DEFAULT_SESSION_URL,
    'attributes': {
        'headers': DEFAULT_SESSION_HEADERS
    }
}
SAMPLE_RESPONSE = {
    "id": "GEE2gmYB8_EXzPlqzPeB",
    "sessionId": "7792158b560cef8004fad9933c74b2401382f06d",
    "samples": [
        {
            "appUsage": 1372571.375,
            "daemonUsage": 0,
            "gbUsage": 12.658227920532227,
            "totalCpuUsage": 39.68846130371094,
            "timestamp": 5257
        }
    ]
}
METRIC_TEST_PARAMS = {
    "no_metric": {
        "metric": "",
        "headers": NO_METRIC_HEADERS,
        "method": "POST",
        "session_id": ""
    },
    "metric_present": {
        "metric": METRIC,
        "headers": DEFAULT_SESSION_HEADERS,
        "method": "GET",
        "session_id": SESSION_ID
    }
}
DEFAULT_EXPECTED_REQUEST_PARAMS = {
    'method': 'GET',
    'url': DEFAULT_SESSION_URL,
    'attributes': {
        'headers': DEFAULT_SESSION_HEADERS,
        'params': 'test_params',
        'data': {
            'test_data': 'test_data'
        }
    }
}
DEFAULT_REQUEST_PARAMS = {
    'method': "GET",
    'session_id': SESSION_ID,
    'metric': METRIC,
    'auth_token': AUTH_TOKEN,
    "params": "test_params",
    "data": {
        "test_data": "test_data"
    }
}
NO_METRIC_REQUEST_PARAMS = {
    'metric': 'app',
    'response': {
        'method': "POST",
        'session_id': SESSION_ID,
        'metric': "",
        'auth_token': AUTH_TOKEN,
        "params": "test_params",
        "data": {
            "test_data": "test_data"
        }
    }
}
NO_METRIC_EXPECTED_REQUEST_PARAMS = {
    'method': 'POST',
    'url': "https://api.production.gamebench.net/v1/sessions/session_id",
    'attributes': {
        'headers': NO_METRIC_HEADERS,
        'params': 'test_params',
        'data': {
            'test_data': 'test_data'
        }
    }
}

# Mock Paths
SESSION_RESPONSE_RETRIEVER_PATH = 'gamebench_api_client.api.response.response_mediator.ResponseRetriever'
REQUEST_BUILDER_PATH = 'gamebench_api_client.api.requests_retriever.builder.request_builder.'
TEST_URL_DIRECTOR_PATH = 'tests.test_unit.test_api' \
                         '.test_requests_retriever.test_builder.test_request_builder.URLDirector'
