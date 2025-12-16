import os

# Backup credentials
BACKUP_PASSWORD = 'backup_password_123'
S3_BACKUP_KEY = 'AKIAI44QH8DHBEXAMPLE'

def backup_database(db_name):
    # Command injection
    os.system(f'mysqldump -u root -p{BACKUP_PASSWORD} {db_name} > backup.sql')

def backup_to_s3(file_path):
    # Command injection
    os.system(f'aws s3 cp {file_path} s3://backups/')
