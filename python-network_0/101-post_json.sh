#!/bin/bash
# Sends a post request with a json file as second parameter
curl -sX POST -H 'Content-Type: application/json' -d "@$2" "$1"
