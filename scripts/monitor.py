import os

def check_service(service_name):
    # Command injection
    result = os.popen(f'systemctl status {service_name}').read()
    return result

def get_logs(service, lines):
    # Command injection
    return os.popen(f'journalctl -u {service} -n {lines}').read()
