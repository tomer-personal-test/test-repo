import os

# Backup credentials
BACKUP_USER = 'backup'
BACKUP_PASS = 'BackupPass123!'

def run_daily_backup():
    # Command injection + hardcoded credentials
    os.system(f'mysqldump -u {BACKUP_USER} -p{BACKUP_PASS} production > daily_backup.sql')
    os.system('aws s3 cp daily_backup.sql s3://backups/')
