#!/usr/bin/python3
"""
    Script uses the requests module to return the body.
"""
import requests


def make_request():
    """
        Function prints out the body of the response in a formatted way.
    """
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    response.encoding = 'utf-8'
    print('Body response:')
    print("\t - type: {}".format(type(response.text)))
    print("\t - content: {}".format(response.text))


if __name__ == "__main__":
    make_request()
