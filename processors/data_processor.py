import pickle
import yaml

class DataProcessor:
    def process_pickle(self, data):
        # Insecure deserialization
        return pickle.loads(data)
    
    def process_yaml(self, data):
        # Unsafe YAML
        return yaml.load(data, Loader=yaml.Loader)
    
    def process_eval(self, expression):
        # Code injection
        return eval(expression)
