#!/usr/bin/env bash

python3 -m pip install --upgrade twine;
python3 -m twine upload --username=$PyPi_UN --password=$PyPi_PW dist/*;
