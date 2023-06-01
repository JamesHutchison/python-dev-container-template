#!/usr/bin/env bash

mkdir -p .dev_container_logs

# run in the background at startup
nohup bash .devcontainer/postStartBackground.sh > ".dev_container_logs/postStartBackground.out" &

# ensure nohup has a chance to run
sleep 3
