#!/usr/bin/python3
"""Task 7. Load, add, save"""

import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

'''
    Adds all arguments to a Python list, and then save them to a file
'''

filename = "add_item.json"

if os.path.exists(filename):
    json_list = load_from_json_file(filename)
else:
    json_list = []

for item in sys.argv[1:]:
    json_list.append(item)

save_to_json_file(json_list, filename)
