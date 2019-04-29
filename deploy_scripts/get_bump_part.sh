#!/usr/bin/env bash


function set_bump_part(){
    if [[ $(git log -1 | grep -cim1 ::patch::) > 0 ]]; then
        BUMP_PART="patch"
    elif [[ $(git log -1 | grep -cim1 ::minor::) > 0 ]]; then
        BUMP_PART="minor";
    elif [[ $(git log -1 | grep -cim1 ::major::) > 0 ]]; then
        BUMP_PART="major";
    else
        BUMP_PART="no bump";
    fi
}

function return_bump_part(){
    echo "${BUMP_PART}";
}

set_bump_part;
return_bump_part;


