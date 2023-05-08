#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request toURL
"""
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    response = requests.post(url, data=data)

    try:
        json_data = response.json()
        if len(json_data) > 0:
            print("[{}] {}".format(json_data["id"], json_data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
