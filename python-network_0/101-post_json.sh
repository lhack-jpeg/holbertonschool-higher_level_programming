#!/bin/bash
# Sends a post request with a json file as second parameter
curl -sX POST -d "@$2" "$1"
