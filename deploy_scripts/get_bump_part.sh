#!/usr/bin/env bash

function get_commit_message(){
    echo "$(git log -1 --pretty=%B)"
}


function set_bump_part(){
    if grep '::patch::' <<< "${COMMIT_MESSAGE}"; then
        BUMP_PART="patch";
    elif grep '::minor::' <<< "${COMMIT_MESSAGE}"; then
        BUMP_PART="minor";
    elif grep '::major::' <<< "${COMMIT_MESSAGE}"; then
        BUMP_PART="major";
    else
        BUMP_PART="no bump";
    fi
}

function return_bump_part(){
    echo "${BUMP_PART}";
}

COMMIT_MESSAGE="$(get_commit_message)";
set_bump_part;
return_bump_part;


