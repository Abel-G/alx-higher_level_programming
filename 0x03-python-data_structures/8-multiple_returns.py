#!/usr/bin/python3

def multiple_returns(sentence):
    i = len(sentence)
    if i == 0:
        first = None
        return i, first
    else:
        first = sentence[0]
        return i, first
