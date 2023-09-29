#!/usr/bin/python3
"""module that fetch a URL"""

import urllib.request

# URL to be fetched
url = 'https://alx-intranet.hbtn.io/status'

# Opens the URL using urllib
with urllib.request.urlopen(url) as response:
    # Reads the content of the response
    html = response.read()

    # Display the body response info
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode('utf-8')))
