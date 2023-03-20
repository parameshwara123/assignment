import yaml
import configparser
import json
import os

def read_config_file(filename):
    """
    Read the given configuration file in YAML, CFG, or CONF format and generate a flat dictionary.
    param filename:string
    """
    config = {}
    with open(filename, 'r') as f:
        ext = os.path.splitext(filename)[1].lower()
        if ext == '.yaml':
            config = yaml.safe_load(f)
        elif ext == '.cfg' or ext == '.conf':
            parser = configparser.ConfigParser()
            parser.read_file(f)
            for section in parser.sections():
                for key, value in parser.items(section):
                    config[f"{key}"] = value
    return config

def write_config_file(filename, config, format='env'):
    """
    Write the given configuration dictionary to the specified file in the specified format.
    Supported formats: env, json
    param filename :string
    param config:dict
    param format:string
    """
    ext = os.path.splitext(filename)[1].lower()
    if format == 'env':
        with open(filename, 'w') as f:
            for key, value in config.items():
                f.write(f"{key}={value}\n")
    elif format == 'json':
        with open(filename, 'w') as f:
            json.dump(config, f)

def set_environment_variables(config):
    """
    Set the given configuration dictionary as environment variables.
    param Config:dict
    """
    for key, value in config.items():
        os.environ[key] = str(value)

file_name = input("Please enter the filename with format extention:")
config = read_config_file(file_name)
print(config)

write_config_file('example.env', config, format='env')
write_config_file('example.json', config, format='json')

set_environment_variables(config)
