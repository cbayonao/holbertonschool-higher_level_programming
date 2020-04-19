#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""


def error_request():

    import requests
    from sys import argv
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)


if __name__ == "__main__":
    error_request()
