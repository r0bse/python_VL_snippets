import os
import sys

from yaml import safe_load


def load_config():
    root_dir = os.path.dirname(sys.modules['__main__'].__file__) # gets root of entry point of script
    with(open(root_dir + "/config.yml", 'r')) as yml:
        return safe_load(yml)


def get_entry() -> str:
    config = load_config()
    value = config["some"]["entry"]
    return value

if __name__ == "__main__":
    print(get_entry())