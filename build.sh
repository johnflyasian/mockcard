#!/bin/bash

docker build -t imagerecdlmock .
docker compose down
docker compose up