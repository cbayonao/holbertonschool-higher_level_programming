#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response (decoded in utf-8).
"""


def postEmail():
    from urllib import request
    from urllib import parse
    from sys import argv

    email = {'email': argv[2]}
    data = parse.urlencode(email)
    dataascii = data.encode('ascii')
    r = request.Request(argv[1], dataascii)
    print(r)
    with request.urlopen(r) as respo:
        print(respo.read().decode("utf-8", "replace"))


if __name__ == "__main__":
    postEmail()
