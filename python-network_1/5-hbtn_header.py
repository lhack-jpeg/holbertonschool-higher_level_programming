#!/usr/bin/python3
"""
    Script uses the requests module to return the X-request-id value
"""
import requests
from sys import argv


def request_id():
    """
        Script uses the requests module to return the X-request-id value
    """
    url = argv[1]
    res = requests.get(url)
    req_id = res.headers.get('X-Request-Id')
    print(req_id)


if __name__ == "__main__":
    request_id()
