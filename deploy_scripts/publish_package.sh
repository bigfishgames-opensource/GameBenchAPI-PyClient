#!/usr/bin/env bash
python3 -m pip install --upgrade twine;
python3 -m twine upload dist/*;
