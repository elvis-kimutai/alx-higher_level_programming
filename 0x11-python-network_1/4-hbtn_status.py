#!/usr/bin/python3
"""
script that fetch 'https://alx-intranet.hbtn.io/status'
"""
import requests

if __name__ == "__main__":
    k = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(k.text)))
    print("\t- content: {}".format(k.text))
