#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.

curl -siL -X OPTIONS "$1" | grep -iF "Allow:" | cut -d " " -f 2-
