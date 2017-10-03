import json
import argparse


def load_data(filepath):
    with open(filepath, 'r') as file_with_json:
        return json.loads(file_with_json.read())


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="write name of json file")
    json_data = load_data(parser.parse_args().file_name)
    pretty_print_json(json_data)
