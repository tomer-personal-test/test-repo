import os
import subprocess

class SystemManagement:
    def restart_service(self, service_name):
        # Command injection
        os.system(f'systemctl restart {service_name}')
    
    def execute_script(self, script_path):
        # Command injection
        subprocess.call(f'bash {script_path}', shell=True)
    
    def cleanup_logs(self, pattern):
        # Command injection
        os.system(f'rm -rf /var/log/{pattern}')
