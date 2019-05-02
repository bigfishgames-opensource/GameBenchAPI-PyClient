A Python Client for the GameBench API

[![Build Status](https://travis-ci.com/bigfishgames/GameBenchAPI-PyClient.svg?branch=master)](https://travis-ci.com/bigfishgames/GameBenchAPI-PyClient)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=bigfishgames_GameBenchAPI&metric=coverage)](https://sonarcloud.io/dashboard?id=bigfishgames_GameBenchAPI)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=bigfishgames_GameBenchAPI&metric=alert_status)](https://sonarcloud.io/dashboard?id=bigfishgames_GameBenchAPI)
[![BCH compliance](https://bettercodehub.com/edge/badge/bigfishgames/GameBenchAPI-PyClient?branch=master)](https://bettercodehub.com/)
[![Gitter](https://badges.gitter.im/bigfishgames/GameBench-API-PyClient.svg)](https://gitter.im/bigfishgames/GameBench-API-PyClient?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Please check out our [ZenHub Board](https://app.zenhub.com/workspaces/gamebenchapi-pyclient-5cabf535a736c27636b0283d/board?repos=180245554) for open issues and feature
requests.

Repository: [GitHub](https://github.com/bigfishgames/GameBenchAPI-PyClient)

For full documentation, go to the [ReadtheDocs](https://gamebenchapi-pyclient.readthedocs.io/) page.

[PyPi](https://pypi.org/project/GameBenchAPI-PyClient-BigFish/#description)

## Overview
To install, run `pip install GameBenchAPI-PyClient-BigFish`

The GameBench API Client library supplies a high-level object-oriented interface to the GameBench API. It is built in
Python 3.7 and uses the Requests library and Pandas data frames to easily integrate into data analysis software.

The library has two main architectural components; the models and API packages. The API package is responsible for
URL requests and dealing with the responses. The models are the objects representing the data returned. A mediator
provides the glue between the api and the models.

As a user of the library, you should only ever need to interact with the models creator class and the model objects
it can return.

Right now, the models are very thin. They only contain a property that has the data frame assigned. Over time we
would like to add common functionality, like aggregates, to these classes.

## The Basics
To make a request, import the ModelCreator class.
Instantiating the ModelCreator requires two arguments.  The first is a CamelCase style 'model'
named after the metric that you are looking for; the model is dynamically imported based on this
name.  The second argument is a dictionary that must include specific key/value pairs for
querying the GameBench API.

```python
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

```
