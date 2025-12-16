from flask import Flask, request, jsonify
import traceback
import sys

app = Flask(__name__)
app.config['DEBUG'] = True  # Vulnerable: debug mode in production

# Information disclosure
@app.route('/error')
def trigger_error():
    try:
        1 / 0
    except Exception as e:
        # Vulnerable: exposing stack trace
        return traceback.format_exc()

@app.route('/config')
def show_config():
    # Vulnerable: exposing configuration
    return jsonify(app.config)

@app.route('/env')
def show_env():
    # Vulnerable: exposing environment variables
    import os
    return jsonify(dict(os.environ))

@app.route('/debug')
def debug_info():
    # Vulnerable: exposing system information
    return {
        'python_version': sys.version,
        'platform': sys.platform,
        'path': sys.path,
        'modules': list(sys.modules.keys())
    }

# Verbose error messages
@app.errorhandler(Exception)
def handle_error(e):
    # Vulnerable: detailed error information
    return {
        'error': str(e),
        'type': type(e).__name__,
        'traceback': traceback.format_exc()
    }, 500
