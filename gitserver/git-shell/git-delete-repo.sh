#!/bin/bash

GIT_DIR="/var/www/git"
USERNAME=$1
REPO_NAME=$2

rm -rf "${GIT_DIR}/${USERNAME}/${REPO_NAME}.git"
echo "Git repository '${REPO_NAME}' deleted in ${GIT_DIR}/${USERNAME}/${REPO_NAME}.git"