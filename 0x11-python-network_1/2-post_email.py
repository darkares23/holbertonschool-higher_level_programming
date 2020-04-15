#!/usr/bin/python3
"""sends a post to the URL and prints the value"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    def getEmail():
        """Post and print the response"""
        url = argv[1]
        values = {'email': argv[2]}

        data = urlencode(values)
        data = data.encode('ascii')
        req = Request(url, data)
        with urlopen(req) as res:
            content = res.read().decode('utf-8')
            print(content)
