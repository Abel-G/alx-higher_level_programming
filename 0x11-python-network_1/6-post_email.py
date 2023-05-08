#!/usr/bin/python3
""" script that takes in a url and and email add. send POST"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
