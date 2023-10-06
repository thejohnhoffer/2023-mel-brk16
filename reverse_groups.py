import sys
import json
import pathlib

def open_json(path):
    with open(path) as f:
        return json.load(f)

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)

def reverse_groups(ex):
    ex["Groups"] = ex["Groups"][::-1]
    return ex

if __name__ == "__main__":
    a = sys.argv[1];
    p = pathlib.Path(a)
    ex = reverse_groups(open_json(p))
    write_json(p, ex)
