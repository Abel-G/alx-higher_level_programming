#!/usr/bin/python3
""" script that takes in a URL, sends request to URL  """
import sys
from urllib import request
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get('X-Request-Id'))
