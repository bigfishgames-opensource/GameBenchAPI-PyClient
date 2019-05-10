#!/usr/bin/env bash

git config --global user.email "travis@travis-ci.com";
git config --global user.name "Travis CI";
git commit -a -m "[skip travis-ci] version bumped!"
git remote rm origin;
git remote add origin https://"$1"@github.com/bigfishgames/GameBenchAPI-PyClient.git > /dev/null 2>&1;
git push origin master;


