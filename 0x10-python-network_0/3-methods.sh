#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -si -L "$1" -X OPTIONS | grep -i Allow | cut -d' ' -f 2-
