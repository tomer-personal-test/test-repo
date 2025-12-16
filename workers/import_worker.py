import yaml
import pickle

class ImportWorker:
    def import_config(self, yaml_data):
        # Unsafe YAML loading
        return yaml.load(yaml_data, Loader=yaml.Loader)
    
    def import_data(self, pickle_data):
        # Insecure deserialization
        return pickle.loads(pickle_data)
