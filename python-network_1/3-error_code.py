#!/usr/bin/python3
"""
    This script sends a request to server and handles any HTTPerror.
"""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys


def http_error():
    """
    Sends through a post request to url and handles any HTTPerrors
    """
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))


if __name__ == '__main__':
    http_error()
