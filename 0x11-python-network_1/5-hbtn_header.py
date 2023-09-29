#!/usr/bin/python3
"""
script that sends a request to the URL & display value of the,
variable X-Request-Id in the response header
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    k = requests.get(url)
    print(k.headers.get("X-Request-Id"))
