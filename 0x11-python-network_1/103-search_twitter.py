#!/usr/bin/python3
import requests
import base64
from sys import argv


if __name__ == "__main__":
    publicKey = argv[1]
    privateKey = argv[2]
    conca = publicKey + ":" + privateKey
    conca = base64.urlsafe_b64encode(conca.encode("ascii")).decode("ascii")
    header = {"Authorization":"Basic{}".format(conca), "Content-type":"application/x-www-form-urlencoded;charset=UTF-8"}
    url = "https://api.twitter.com/oauth2/token"
    _data = {"grant_type" : "client_credentials"}
    req = requests.post(url, headers=header, data=_data).json()
    print(req.get('access_token'))
