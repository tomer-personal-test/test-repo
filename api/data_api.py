from flask import Flask, request
import yaml
import json

app = Flask(__name__)

@app.route('/api/parse_yaml', methods=['POST'])
def parse_yaml():
    data = request.data
    # Unsafe YAML loading
    return yaml.load(data, Loader=yaml.Loader)

@app.route('/api/eval')
def eval_code():
    code = request.args.get('code')
    # Code injection
    return str(eval(code))

@app.route('/api/exec')
def exec_code():
    code = request.args.get('code')
    # Code injection
    exec(code)
    return 'OK'
