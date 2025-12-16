from flask import Flask, request, jsonify
import sys
import os

app = Flask(__name__)
app.config['DEBUG'] = True  # Debug mode in production

@app.route('/debug/env')
def debug_env():
    # Information disclosure
    return jsonify(dict(os.environ))

@app.route('/debug/config')
def debug_config():
    # Information disclosure
    return jsonify(dict(app.config))

@app.route('/debug/eval')
def debug_eval():
    code = request.args.get('code')
    # Code injection
    return str(eval(code))
