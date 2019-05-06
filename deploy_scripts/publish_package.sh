#!/usr/bin/env bash

python3 -m pip install --upgrade twine;
python3 -m twine upload --username="$1" --password="$2" --verbose dist/*;
