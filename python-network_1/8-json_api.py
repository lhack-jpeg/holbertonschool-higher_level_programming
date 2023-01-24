#!/usr/bin/python3
"""
    Script sends a post request to url with the letter as parameter
"""
import requests
from sys import argv


def search_api(q=""):
    """
    Letter will sent under the variable 'q'. If the response is properly
    formatted JSON will return a display of [<id>] <name>.
    """
    try:
        q = argv[1]
    except IndexError as e:
        pass
    post_data = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url, data=post_data)
    print(res.json())


if __name__ == "__main__":
    search_api()
