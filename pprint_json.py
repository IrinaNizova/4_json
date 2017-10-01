import json
import sys
import pprint


def load_data(filepath):
    try:
        file = open(filepath, 'r')
        json_data = json.loads(file.read())
        pretty_print_json(json_data)
    finally:
        file.close()


def pretty_print_json(data):
    pretty_format_data = pprint.PrettyPrinter(indent=1)
    pretty_format_data.pprint(data)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('you did not write file name')
    else:
        load_data(sys.argv[1])
