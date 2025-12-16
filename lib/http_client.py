import requests
import urllib.request
import ssl

class HTTPClient:
    def get(self, url, verify_ssl=False):
        # SSRF + insecure SSL
        return requests.get(url, verify=verify_ssl)
    
    def post(self, url, data):
        # SSRF
        return requests.post(url, json=data)
    
    def fetch(self, url):
        # SSRF + insecure SSL
        context = ssl._create_unverified_context()
        return urllib.request.urlopen(url, context=context).read()
