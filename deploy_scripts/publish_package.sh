#!/usr/bin/env bash
cd ..;
python3 -m pip install --upgrade twine;
python3 -m twine upload dist/*;
