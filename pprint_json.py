import json
import sys
import pprint


def load_data(filepath):
    try:
        text = open(filepath, 'r')
        json_data = json.loads(text.read())
        pretty_print_json(json_data)
    finally:
        text.close()


def pretty_print_json(data):
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(data)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('you did not write file name')
    else:
        load_data(sys.argv[1])
