Overview
========

The GameBench API client library enables automatic delivery of performance data from the GameBench API back to the client.   It is built in Python 3.7 and uses the Requests python library to construct HTTP traffic.

The client simply passes in a dictionary to the library that includes the information they want from the GameBenchAPI.  The library will do the rest and return the requested data as a Pandas DataFrame for the client to use.
