#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        data = load_from_json_file("add_item.json")
    except:
        new_obj = []
        f =open("add_item.json", 'w')
        save_to_json_file(new_obj, "add_item.json")
        f.close()

    data = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        data.append(sys.argv[i])
    save_to_json_file(data, "add_item.json")
