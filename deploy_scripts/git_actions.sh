#!/usr/bin/env bash

git config --global user.email "travis@travis-ci.com";
git config --global user.name "Travis CI";

git stash;

git checkout master;

git stash pop --quiet;
git commit --all -m "[skip travis-ci] version bumped!";

git remote rm origin;
git remote add origin https://aaron-wilson-bfg:"$1"@github.com/bigfishgames/GameBenchAPI-PyClient.git > /dev/null 2>&1;

git push -u origin master --quiet;
