#!/bin/bash

TEST_DIR="$(dirname "$(realpath "$0")")"
GIT_DIR="$(dirname "$TEST_DIR")"

DOCKER="${1:-docker}"
IMAGE="ghcr.io/home-assistant/home-assistant:stable"
NAME="HA_test_integration"
PORT="8123"

set -e

echo "Starting HA container $NAME"
$DOCKER create \
  --rm \
  --name "$NAME" \
  --publish "127.0.0.1:$PORT:$PORT" \
  --volume "$TEST_DIR/configuration.yaml:/config/configuration.yaml" \
  --volume "$TEST_DIR/entities:/config/entities" \
  --volume "$GIT_DIR:/config/custom_components/energy_meter" \
  "$IMAGE" > /dev/null

$DOCKER cp "$TEST_DIR/config" "$NAME:/"

$DOCKER start "$NAME"

echo "HA container is accessible on http://127.0.0.1:$PORT"
echo "Credentials are test:test"
