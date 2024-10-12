#!/usr/bin/env python3

import json

import yaml


def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            if file_path.endswith(".json"):
                return json.load(file)
            elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
                return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        print(f"Error: File '{file_path}' is not a valid JSON or YAML. {e}.")
        return None
