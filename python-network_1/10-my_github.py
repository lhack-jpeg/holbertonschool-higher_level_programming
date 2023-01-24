#!/usr/bin/python3
"""
This Script take github credentials and and use the github api to print
out the user id.
"""
import requests
from sys import argv


def get_github_id():
    """
    The function uses the github user name and personal access token to
    retrieve and print out the user id
    """
    username = argv[1]
    pat = argv[2]
    url = 'https://api.github.com/users/{}'.format(username)
    headers = {"Authorization": "Bearer {}".format(
        pat), "Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(None)
    else:
        json_res = response.json()
        print(json_res.get('id'))


if __name__ == "__main__":
    get_github_id()
