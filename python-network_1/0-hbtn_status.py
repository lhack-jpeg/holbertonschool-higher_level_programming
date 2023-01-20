#!/usr/bin/python3
"""This script fetches a url and prints out the body."""
import urllib.request


def url_fetcher():
    """Function prints out information about the status of the server."""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    url_fetcher()
