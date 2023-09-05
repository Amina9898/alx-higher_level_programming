#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import sys
import urllib.request
import urllib.error

URL = sys.argv[1]

request = urllib.request.Request(URL)

try:
    with urllib.request.urllibopen(request) as response:
        print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
