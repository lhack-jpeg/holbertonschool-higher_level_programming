#!/bin/bash
#Takes in a URL and sends an address and returns the size of it
curl -s --head "$1" | grep "Content-Length" | cut -d " " -f 2
