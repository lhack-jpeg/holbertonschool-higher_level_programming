#!/bin/bash
# Script displays body of only 200 responses. Follows redirects
curl -X GET  "$1" -L
