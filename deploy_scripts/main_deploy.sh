#!/usr/bin/env bash

./deploy_scripts/bump_version.sh;
./deploy_scripts/build_package.sh;
./deploy_scripts/publish_package.sh "$1" "$2";
./deploy_scripts/git_actions.sh "$3";

exit

