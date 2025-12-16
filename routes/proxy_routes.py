from flask import Flask, request
import requests
import urllib.request

app = Flask(__name__)

@app.route('/proxy/get')
def proxy_get():
    url = request.args.get('url')
    # SSRF
    return requests.get(url).text

@app.route('/proxy/post')
def proxy_post():
    url = request.args.get('url')
    data = request.json
    # SSRF
    return requests.post(url, json=data).text

@app.route('/proxy/fetch')
def proxy_fetch():
    url = request.args.get('url')
    # SSRF
    return urllib.request.urlopen(url).read()
