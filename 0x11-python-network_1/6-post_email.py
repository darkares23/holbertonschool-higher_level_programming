#!/usr/bin/python3
"""s takes in a URL and an email address,
sends a POST request to the passed URL"""
import requests
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    req = requests.post(argv[1], data=values)
    print(req.text)
