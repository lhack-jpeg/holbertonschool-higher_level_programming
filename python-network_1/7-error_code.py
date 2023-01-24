#!/usr/bin/python3
"""
    Use requests module to handle HTTPerror codes.
"""
import requests
from requests import HTTPError
from sys import argv


def http_error():
    """
        Handles HTTPerror codes from requests
    """
    url = argv[1]

    response = requests.get(url)
    if response.status_code != 200:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    http_error()
