#!/usr/bin/bash
# bash script that takes in URL send GET request and display ist body
curl -s -L "$1" -X GET
