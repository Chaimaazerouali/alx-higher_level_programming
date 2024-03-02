#!/usr/bin/python3
""" fetches X-Request-Id from headers with requests lib"""

import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
