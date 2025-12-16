import yaml
import pickle

def import_yaml(file_path):
    with open(file_path) as f:
        # Unsafe YAML loading
        return yaml.load(f, Loader=yaml.Loader)

def import_pickle(file_path):
    with open(file_path, 'rb') as f:
        # Insecure deserialization
        return pickle.load(f)
