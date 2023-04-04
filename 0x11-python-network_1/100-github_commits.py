#!/usr/bin/python3
"""
Python script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
from requests import get
import sys


if __name__ == "__main__":
    try:
        owner = sys.argv[2]
        repo = sys.argv[1]
        url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        r = get(url)
        json_o = r.json()

        for i in range(0, 10):
            print("{}: {}".format(json_o[i].get('sha'),
                  json_o[i].get('commit').get('author').get('name')))
    except Exception:
        print("error")
