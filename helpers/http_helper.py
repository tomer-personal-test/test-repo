import requests
import urllib.request
import ssl

class HTTPHelper:
    def fetch(self, url):
        # SSRF + insecure SSL
        context = ssl._create_unverified_context()
        return urllib.request.urlopen(url, context=context).read()
    
    def post(self, url, data):
        # SSRF
        return requests.post(url, json=data, verify=False).text
