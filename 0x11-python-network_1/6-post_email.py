#!/usr/bin/python3
"""
script that sends a POST request to the passed URL with the email
as a parameter,& displaysthe body of the response
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    k = requests.post(url, data=value)
    print(k.text)
