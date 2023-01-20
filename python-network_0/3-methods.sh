#!/bin/bash
# Returns the allow methods on a server
curl -sX OPTIONS "$1" --head | grep "Allow" | cut -d " " -f 2-
