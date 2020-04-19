#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter.
"""


def search_api():
    import requests
    import sys

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json = req.json()
        if json == {}:
            print('No result')
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except ValueError:
        print('Not a valid JSON')


if __name__ == "__main__":
    search_api()
