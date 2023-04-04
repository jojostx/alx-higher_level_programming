#!/usr/bin/python3
""" Sends a request to a URL and
displays the value of the X-Request-Id header """

import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(url) as r:
        print(r.getheader('X-Request-Id'))
