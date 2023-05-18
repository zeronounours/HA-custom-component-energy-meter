#!/bin/bash

DOCKER="${1:-docker}"
NAME="HA_test_integration"

echo "Stop HA container $NAME"
$DOCKER stop "$NAME"
