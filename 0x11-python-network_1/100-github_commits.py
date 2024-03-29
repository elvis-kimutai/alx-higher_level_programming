#!/usr/bin/python3
"""
script that take two arguments; 'repository name' &
'owner name', in order to solve HBTN GitHub challenge
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    k = requests.get(url)
    commits = k.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
