#!/usr/bin/env bash
cd ..;
python3 -m pip install --upgrade setuptools wheel;
python3 setup.py sdist bdist_wheel;

