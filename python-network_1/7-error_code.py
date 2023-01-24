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
    try:
        response = requests.get(url)
        print(response.text)
    except HTTPError as error:
        print("Error code: {}".format(error))


if __name__ == "__main__":
    http_error()
