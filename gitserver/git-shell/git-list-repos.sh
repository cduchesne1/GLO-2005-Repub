#!/bin/bash
GIT_DIR="/var/www/git"
USERNAME=$1

for REPO in ${GIT_DIR}/${USERNAME}/*
do
  printf '%s\n' "$(basename ${REPO%.git})"
done