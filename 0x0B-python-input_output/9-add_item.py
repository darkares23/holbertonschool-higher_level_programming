#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        data = load_from_json_file("add_item.json")
        save_to_json_file(new_obj, "add_item.json")
    except:
        save_to_json_file(sys.argv[1:], "add_item.json")
