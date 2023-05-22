#!/bin/bash

if [ -n "${1:+}" ]; then
  DOCKER="${1}"
elif which podman &> /dev/null; then
  DOCKER="podman"
else
  DOCKER="docker"
fi
NAME="HA_test_integration"

echo "Stop HA container $NAME"
$DOCKER stop "$NAME"
