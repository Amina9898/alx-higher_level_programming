#!/usr/bin/python3
"""Sends a request to a given URL and displays the response"""

import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]

    response = requests.get(URL)
    if response.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(response.text)
