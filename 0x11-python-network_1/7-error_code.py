#!/usr/bin/python3
"""
script that send a request to URL & display
body of the response
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    k = requests.get(url)
    if k.status_code >= 400:
        print("Error code: {}".format(k.status_code))
    else:
        print(k.text)
