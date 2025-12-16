import pickle
import yaml

class SerializationHelper:
    def serialize(self, obj):
        # Insecure serialization
        return pickle.dumps(obj)
    
    def deserialize(self, data):
        # Insecure deserialization
        return pickle.loads(data)
    
    def load_yaml(self, yaml_str):
        # Unsafe YAML
        return yaml.load(yaml_str, Loader=yaml.Loader)
