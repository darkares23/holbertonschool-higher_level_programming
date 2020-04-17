#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import requests
from sys import argv


if __name__ == "__main__":
    aut = argv[2]
    url = "https://api.github.com/repos/" + aut + "/" + argv[1] + "/commits"
    req = requests.get(url).json()
    commits = 0
    for line in req:
        print("{}: {}".format(line['sha'], line['commit']['author']['name']))
        commits += 1
        if commits == 10:
            exit()
