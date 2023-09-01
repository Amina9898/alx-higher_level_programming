#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id 
variable found in the header of the response.
"""


import urllib
import sys


if __name__ == "__main__":
    URL = sys.argv[1]

    request = urllib.request.Request(URL)
    with urllib.request.Request(URL) as response:
        print(dict(response.headers).get("X-Request-Id"))
