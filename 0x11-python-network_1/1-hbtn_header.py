#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import urllib.request
import sys


def getRequest():
    """a"""
    with urllib.request.urlopen(sys.argv[1]) as res:
        req = res.headers.get('X-Request-Id')
        print(req)

if __name__ == "__main__":
    getRequest()
