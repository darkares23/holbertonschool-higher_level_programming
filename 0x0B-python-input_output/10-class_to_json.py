#!/bin/usr/python3
def class_to_json(obj):
    if hasattr(obj, '__dic__'):
        return obj.__dic__
