#!/usr/bin/python3
"""
 scri that takes URL sends a request\
 to the URL and displays the body of responce
"""

import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.content)