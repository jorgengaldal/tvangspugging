import yaml
import json


def json_config():
    with open("config.json") as file:
        return json.load(file)


def yaml_config():
    with open("config.yml", "r") as file:
        return yaml.safe_load(file)


def config():
    """Uses config.yml file by default."""
    return yaml_config()
