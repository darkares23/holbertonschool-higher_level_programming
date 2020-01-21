#!/usr/bin/python3
import json
from sys import argv
import os
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


my_list = []
if os.path.isfile('add_item.json') is True:
    my_list = load_from_json_file('add_item.json')
for i in range(1, len(argv)):
    my_list.append(argv[i])
save_to_json_file(my_list, 'add_item.json')
