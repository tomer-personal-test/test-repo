import os
import subprocess

class ExportTask:
    def export_database(self, format):
        # Command injection
        os.system(f'export_db.sh --format={format}')
    
    def export_files(self, path, destination):
        # Command injection
        subprocess.call(f'rsync -av {path} {destination}', shell=True)
