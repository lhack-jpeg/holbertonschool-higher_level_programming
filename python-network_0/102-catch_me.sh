#!/bin/bash
# Script tries to get server to respond with catch me
curl -LX PUT 0.0.0.0:5000/catch_me -F "user_id=98"
