#!/bin/bash
GIT_DIR="/var/www/git"
USERNAME=$1
REPO_NAME=$2
BRANCH_NAME=$3

cd ${GIT_DIR}/${USERNAME}/${REPO_NAME}.git

git config --global --add safe.directory "${GIT_DIR}/${USERNAME}/${REPO_NAME}.git"
git ls-tree -r ${BRANCH_NAME} --name-only
