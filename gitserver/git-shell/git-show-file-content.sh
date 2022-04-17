#!/bin/bash
GIT_DIR="/var/www/git"
USERNAME=$1
REPO_NAME=$2
BRANCH=$3
FILE_PATH=$4

cd ${GIT_DIR}/${USERNAME}/${REPO_NAME}.git

git config --global --add safe.directory "${GIT_DIR}/${USERNAME}/${REPO_NAME}.git"
git show ${BRANCH}:${FILE_PATH}