A Python Client for the GameBench API

[![Build Status](https://travis-ci.com/bigfishgames/GameBenchAPI-PyClient.svg?branch=master)](https://travis-ci.com/bigfishgames/GameBenchAPI-PyClient)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=bigfishgames_GameBenchAPI&metric=coverage)](https://sonarcloud.io/dashboard?id=bigfishgames_GameBenchAPI)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=bigfishgames_GameBenchAPI&metric=alert_status)](https://sonarcloud.io/dashboard?id=bigfishgames_GameBenchAPI)
[![BCH compliance](https://bettercodehub.com/edge/badge/bigfishgames/GameBenchAPI-PyClient?branch=master)](https://bettercodehub.com/)
[![Gitter](https://badges.gitter.im/bigfishgames/GameBench-API-PyClient.svg)](https://gitter.im/bigfishgames/GameBench-API-PyClient?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Please check out our [ZenHub Board](https://app.zenhub.com/workspaces/gamebenchapi-pyclient-5cabf535a736c27636b0283d/board?repos=180245554) for open issues.

For full documentation, go to the [ReadtheDocs](https://gamebenchapi-pyclient.readthedocs.io/) page.

##Overview
The GameBench API Client library enables automatic delivery of performance data from the GameBench API back to the client. It is built in Python 3.7 and uses the Requests python library to construct HTTP traffic.

The client simply passes in a dictionary to the library that includes the information they want from the GameBenchAPI. The library will do the rest and return the requested data as a Pandas DataFrame for the client to use.

##The Basics
All requests to the GameBench API Client will go through the `ModelCreator` class.  This class
is instantiated and given a

```python
from gamebench_api_client.models.creator.model_creator import ModelCreator



time_series_request = {
    'session_id': '66d926f47ff5a7a5d853d1058c6305614e1ae6a5',
    'metric': '/cpu',
    'detail': '',
    'params': '',
    'data': '',
}

creator = ModelCreator('Cpu', time_series_request)
cpu_time_series = creator.get_model()

results = cpu_time_series.data

print(results)

"""
      appUsage  daemonUsage    gbUsage  timestamp  totalCpuUsage
0  1372571.375            0  12.658228       5257      39.688461
"""

```

[GitHub](https://github.com/bigfishgames/GameBenchAPI-PyClient)
