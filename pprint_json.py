import json
import sys
import pprint


def load_data(filepath):
    try:
        file_with_json = open(filepath, 'r')
        json_data = json.loads(file_with_json.read())
        pretty_print_json(json_data)
    finally:
        file_with_json.close()


def pretty_print_json(json_data):
    pretty_format_data = pprint.PrettyPrinter(indent=1)
    pretty_format_data.pprint(json_data)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('you did not write file name')
    else:
        load_data(sys.argv[1])
