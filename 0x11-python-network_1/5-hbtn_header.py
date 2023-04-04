#!/usr/bin/python3
""" Sends a request to a URL and
displays the value of the X-Request-Id header """

import requests
import sys

url = sys.argv[1]

if __name__ == "__main__":
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))
