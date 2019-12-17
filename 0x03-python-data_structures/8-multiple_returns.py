#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == 0:
        _1char = None
    else:
        _1char = sentence[0]
    return (len(sentence), _1char)
