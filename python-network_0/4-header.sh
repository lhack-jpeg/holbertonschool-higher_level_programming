#!/bin/bash
# Sends a get request with a header defined
curl -sX GET "$1" -H "X-School-User-Id: 98"
