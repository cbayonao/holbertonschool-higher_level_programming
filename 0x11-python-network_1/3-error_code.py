#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


def error_code():
    import sys
    from urllib import request
    from urllib.error import HTTPError

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode("utf-8", "replace"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))


if __name__ == "__main__":
    error_code()
