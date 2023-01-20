#!/bin/bash
# Sends a post request to URL and displays body of the response
curl -sX POST "$1" -F "email=test@gmail.com" -F "subject:I will always be here for PLD"
