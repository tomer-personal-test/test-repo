import os
import shutil

def cleanup_temp_files(pattern):
    # Command injection
    os.system(f'rm -rf /tmp/{pattern}')

def cleanup_logs(days):
    # Command injection
    os.system(f'find /var/log -mtime +{days} -delete')

def cleanup_directory(path):
    # Path traversal
    shutil.rmtree(path)
