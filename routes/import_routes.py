from flask import Flask, request
import yaml
import pickle

app = Flask(__name__)

@app.route('/import/yaml', methods=['POST'])
def import_yaml():
    data = request.data
    # Unsafe YAML loading
    config = yaml.load(data, Loader=yaml.Loader)
    return str(config)

@app.route('/import/pickle', methods=['POST'])
def import_pickle():
    data = request.data
    # Insecure deserialization
    obj = pickle.loads(data)
    return str(obj)
