from argparse import Namespace

import yaml


def load_config(yaml_file: str):
    with open(yaml_file) as f:
        config = yaml.safe_load(f)
    return Namespace(**config)
