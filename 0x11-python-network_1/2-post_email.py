#!/usr/bin/python3
"""sends a post to the URL and prints the value"""
import urllib.request
import urllib.parse
from sys import argv


def getRequest():
    """Post and print the response"""
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('utf-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as res:
        content = res.read()
        print(content.decode('utf-8'))

if __name__ == "__main__":
    getRequest()
