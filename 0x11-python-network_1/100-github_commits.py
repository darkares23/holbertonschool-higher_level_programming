#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/" + argv[2] + "/" + argv[1] + "/commits"
    _auth = (argv[1], argv[2])
    req = requests.get(url).json()
    commits = 0
    for line in req:
        print("{}: {}".format(line['sha'], line['commit']['author']['name']))
        commits += 1
        if commits == 10:
            exit()
