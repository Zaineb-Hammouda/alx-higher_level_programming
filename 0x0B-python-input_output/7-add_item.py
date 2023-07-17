#!/usr/bin/python3
"""
using the 5-save_to_json_file and 6-load_from_json_file modules
"""

import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

with open("add_item.json", "a+", encoding="utf-8") as f:
    if f.tell() == 0:
        save_to_json_file([], "add_item.json")

j_list = load_from_json_file("add_item.json")

if len(sys.argv) > 1:
    for i in range(len(sys.argv) - 1):
        x = sys.argv[i + 1]
        j_list.append(x)

save_to_json_file(j_list, "add_item.json")
