#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''
    _data = {'q': q}
    req = requests.post('http://0.0.0.0:5000/search_user', data=_data).json()
    try:
        if len(req) == 0:
            print("No result")
            exit()
        print ("[{}] {}".format(req.get('id'), req.get('name')))
    except ValueError:
        print("Not a valid JSON")
