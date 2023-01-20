#!/bin/bash
# Returns the status code of the url
curl -s -o /dev/null -w "%{http_code}" "$1"
