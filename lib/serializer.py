import pickle
import yaml
import json

class Serializer:
    def serialize(self, obj):
        # Insecure serialization
        return pickle.dumps(obj)
    
    def deserialize(self, data):
        # Insecure deserialization
        return pickle.loads(data)
    
    def load_yaml(self, yaml_string):
        # Unsafe YAML loading
        return yaml.load(yaml_string, Loader=yaml.Loader)
    
    def load_yaml_unsafe(self, yaml_string):
        # Unsafe YAML loading
        return yaml.unsafe_load(yaml_string)
