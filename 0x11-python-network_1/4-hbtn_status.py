#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and"""
import requests


def getStatus():
    req = requests.get('https://intranet.hbtn.io/status')
    content = req.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- utf8 content: {}".format(content.decode('utf-8')))

if __name__ == "__main__":
    getStatus()
