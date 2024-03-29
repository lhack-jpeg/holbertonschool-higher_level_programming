#!/usr/bin/python3
"""
    This script sends a post request to a server
    with the email parameter sent through.
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


def post_email():
    """
    Sends through a post request to url.
    """
    url = sys.argv[1]
    email = sys.argv[2]
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    post_data = {"email": email}
    url_encoded_data = urlencode(post_data)
    post_data = url_encoded_data.encode("utf-8")
    post_request = Request(url, headers=headers, data=post_data, method="POST")
    with urlopen(post_request) as response:
        server_res = response.read()
        print(server_res.decode('utf-8'))


if __name__ == '__main__':
    post_email()
