#!/bin/bash
# Script displays body of only 200 responses. Follows redirects
curl -sX GET  "$1" -L
