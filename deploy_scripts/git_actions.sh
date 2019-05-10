#!/usr/bin/env bash

git commit --all -m "[skip travis-ci] version bumped!";
git remote rm origin;
git remote add origin https://aaron-wilson-bfg:"$1"@github.com/bigfishgames/GameBenchAPI-PyClient.git;
git push origin master;
