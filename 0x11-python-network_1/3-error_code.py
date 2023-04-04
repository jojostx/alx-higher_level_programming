#!/usr/bin/python3
""" Sends a request to a URL and
displays the value of the X-Request-Id header """

import sys
from urllib import request, parse
from urllib.error import HTTPError

if __name__ == "__main__":
    req = request.Request(sys.argv[1])

    try:
        with request.urlopen(req) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
