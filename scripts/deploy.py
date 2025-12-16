import os
import subprocess

# Deployment credentials
DEPLOY_KEY = 'deploy_key_1234567890abcdef'
SSH_KEY = '-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA...'

def deploy(environment, branch):
    # Command injection
    os.system(f'git checkout {branch}')
    os.system(f'deploy.sh {environment}')

def restart_services(service_name):
    # Command injection
    subprocess.call(f'systemctl restart {service_name}', shell=True)
