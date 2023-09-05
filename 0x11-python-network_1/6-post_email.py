#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email"""

import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]
    output = {"email": sys.argv[2]}

    response = requests.post(URL, data=output)
    print(response.text)
