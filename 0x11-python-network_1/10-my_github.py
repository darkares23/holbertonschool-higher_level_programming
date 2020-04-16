#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    _auth = (argv[1], argv[2])
    req = requests.get(url, auth=_auth).json()
    reqId = req.get('id')
    print(reqId)
