#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response"""


def header_req():
    import requests
    import sys
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))


if __name__ == "__main__":
    header_req()
