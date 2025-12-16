import os

def cleanup_temp_files():
    # Command injection
    os.system('find /tmp -type f -mtime +7 -delete')

def cleanup_old_logs():
    # Command injection
    os.system('find /var/log -type f -mtime +30 -delete')
