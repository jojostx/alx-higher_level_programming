#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == "__main__":
    res = requests.get(url)
    t = res.text
    print('Body response:')
    print('\t- type: {}'.format(type(t)))
    print('\t- content: {}'.format(t))
