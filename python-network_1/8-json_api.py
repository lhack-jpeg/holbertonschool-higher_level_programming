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
    try:
        json_res = res.json()
        id = json_res.get('id')
        name = json_res.get('name')
        if id is None or name is None:
            print('No Result')

        print('[{}] {}'.format(id, name))
    except Exception as e:
        print(e)
        print('Not a valid JSON')


if __name__ == "__main__":
    search_api()
