#!/usr/bin/env bash

git config --global user.email "travis@travis-ci.com";
git config --global user.name "Travis CI";
git add .;
git commit --message "[skip travis-ci] version bumped!";
git remote rm origin;
git remote add origin https://aaron-wilson-bfg:"$1"@github.com/bigfishgames/GameBenchAPI-PyClient.git;
git push origin master;
