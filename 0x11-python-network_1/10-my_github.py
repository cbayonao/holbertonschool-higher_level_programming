#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API
to display your id
"""


def req_github_credentials():
    import requests
    import sys

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))


if __name__ == "__main__":
    req_github_credentials()
