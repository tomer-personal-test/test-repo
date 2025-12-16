import os

def check_services():
    services = ['nginx', 'mysql', 'redis']
    for service in services:
        # Command injection
        status = os.popen(f'systemctl status {service}').read()
        if 'active' not in status:
            # Command injection
            os.system(f'systemctl restart {service}')
