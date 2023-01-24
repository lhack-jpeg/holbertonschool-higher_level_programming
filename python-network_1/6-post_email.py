#!/usr/bin/python3
"""
    Script uses the requests module to post to a url
"""
import requests
from sys import argv


def post_email():
    """
        Script uses the requests module to post to a url and send email value
        through.
    """
    url = argv[1]
    email = argv[2]
    post_data = {"email": email}
    response = requests.post(url, data=post_data)
    print(response.text)


if __name__ == "__main__":
    post_email()
