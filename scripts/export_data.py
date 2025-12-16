import os

def export_database(format, output):
    # Command injection
    os.system(f'export_db.sh --format={format} --output={output}')

def export_users(filename):
    # Command injection
    os.system(f'mysql -e "SELECT * FROM users" > {filename}')
