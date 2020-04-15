#!/usr/bin/python3
"""s takes in a URL and an email address,
sends a POST request to the passed URL"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print('Error code: {}'.format(req.status_code))
    else:
        print(req.text)
