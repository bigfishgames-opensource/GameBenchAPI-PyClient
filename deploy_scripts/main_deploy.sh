#!/usr/bin/env bash

bash bump_version.sh;
bash build_package.sh;
bash publish_package.sh;

