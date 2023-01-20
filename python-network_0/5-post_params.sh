#!/bin/bash
# Sends a post request to URL and displays body of the response
curl -sX POST "$1" -H 'Content-Type: application/json' -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}'
