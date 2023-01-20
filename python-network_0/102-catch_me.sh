#!/bin/bash
# Script tries to get server to respond with catch me
curl -sLX PUT 0.0.0.0:5000/catch_me -F "user_id=98" -H "Origin: HolbertonSchool"
