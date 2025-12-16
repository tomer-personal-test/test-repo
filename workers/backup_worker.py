import os
import subprocess

class BackupWorker:
    def backup_database(self, db_name):
        # Command injection
        os.system(f'mysqldump {db_name} > backup.sql')
    
    def backup_files(self, path):
        # Command injection
        subprocess.call(f'tar -czf backup.tar.gz {path}', shell=True)
