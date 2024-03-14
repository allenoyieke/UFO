# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
import yaml


def load_config(config_path="ufo/config/config.yaml"):
    """
    Load the configuration from a YAML file and environment variables.

    :param config_path: The path to the YAML config file. Defaults to "./config.yaml".
    :return: Merged configuration from environment variables and YAML file.
    """

    configuration = dict()

    try:
        with open(config_path, "r") as file:
            yaml_configuration = yaml.safe_load(file)
        # Update configs with YAML data
        if yaml_configuration:
            configuration.update(yaml_configuration)

    except FileNotFoundError:
        print(f"Warning: Config file not found at {config_path}. Using only environment variables.")

    env_configuration = dict(os.environ)

    # Override static file configuration with environment variables
    configuration.update(env_configuration)

    return configuration