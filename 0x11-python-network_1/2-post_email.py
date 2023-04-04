#!/usr/bin/python3
""" Sends a request to a URL and
displays the value of the X-Request-Id header """

import sys
from urllib import request, parse

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))
