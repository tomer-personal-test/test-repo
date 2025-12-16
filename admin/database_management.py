import os

# Database admin credentials
DB_ADMIN_USER = 'dbadmin'
DB_ADMIN_PASS = 'DbAdmin123!'

class DatabaseManagement:
    def backup_database(self, db_name):
        # Command injection + hardcoded password
        os.system(f'mysqldump -u {DB_ADMIN_USER} -p{DB_ADMIN_PASS} {db_name} > backup.sql')
    
    def restore_database(self, db_name, backup_file):
        # Command injection
        os.system(f'mysql -u {DB_ADMIN_USER} -p{DB_ADMIN_PASS} {db_name} < {backup_file}')
