#!/usr/bin/python3
"""This script prints out the value of the X-request-id"""
import urllib.request
import sys


def request_id():
    """This function returns the value of the request id."""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-request-Id"))


if __name__ == "__main__":
    request_id()
