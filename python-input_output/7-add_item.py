#!/usr/bin/python3
'''
This script gets command line arguments adds them
to a json file
'''

import sys
import json


def main():
    file_name = 'add_item.json'
    list_obj = []
    argc = len(sys.argv) - 1
    args = []
    for i in range(1, argc + 1):
        args.append(sys.argv[i])

    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            list_obj = json.load(f)
    except Exception as e:
        pass

    list_obj.extend(args)
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(list_obj, f)


if __name__ == '__main__':
    main()
