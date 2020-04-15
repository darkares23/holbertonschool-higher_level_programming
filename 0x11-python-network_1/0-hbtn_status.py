#!/usr/bin/python3
"""Python script that fetches"""
import urllib.request


def getStatus():
    """a"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        type_content = type(content)
        print("Body response:")
        print("\t- type: {}".format(type_content))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))

if __name__ == "__main__":
    getStatus()
