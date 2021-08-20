#!/usr/bin/env python
import json
import pathlib
import yaml
from yaml.loader import SafeLoader


def get_file_extension(file_path):
    return pathlib.Path(file_path).suffix


def load_data_from_json(file_path):
    with open(file_path) as f:
        return json.load(f)


def load_data_from_yaml(file_path):
    with open(file_path) as f:
        return yaml.load(f, Loader=SafeLoader)


def load_data(file_path):
    extension = get_file_extension(file_path)
    if extension in ['.yml', '.yaml']:
        return load_data_from_yaml(file_path)
    if extension == '.json':
        return load_data_from_json(file_path)
