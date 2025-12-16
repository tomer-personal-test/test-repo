import requests
import urllib.request
import ssl

def fetch_url(url):
    # SSRF
    return requests.get(url).text

def fetch_with_ssl(url):
    # Insecure SSL
    context = ssl._create_unverified_context()
    return urllib.request.urlopen(url, context=context).read()

def post_data(url, data):
    # SSRF
    return requests.post(url, json=data).text
