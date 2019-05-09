#!/usr/bin/env bash

git_config() {
    git config --global user.email "travis@travis-ci.com";
    git config --global user.name "Travis CI";
}

git_commit() {
    git commit -m "[skip travis-ci] version bumped!";
}

git_push() {
    git remote rm origin;
    git remote add origin https://"$3"@github.com/bigfishgames/GameBenchAPI-PyClient.git > /dev/null 2>&1
    git push origin master --quiet;
}

git_config;
git_commit;
git_push;
