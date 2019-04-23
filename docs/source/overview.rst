Overview
========

The GameBench API Client library supplies a high-level object-oriented interface to the GameBench API. It is built in
Python 3.7 and uses the Requests library and Pandas data frames to easily integrate into data analysis software.

The library has two main architectural components; the models and API packages. The API package is responsible for
URL requests and dealing with the responses. The models are the objects representing the data returned. A mediator
provides the glue between the api and the models.

As a user of the library, you should only ever need to interact with the models creator class and the model objects
it can return.

Right now, the models are very thin. They only contain a property that has the data frame assigned. Over time we
would like to add common functionality, like aggregates, to these classes.
