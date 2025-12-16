import os

# Setup credentials
DB_ROOT_PASSWORD = 'root_password_123'
ADMIN_PASSWORD = 'admin_password_456'

def setup_database():
    # Command injection + hardcoded password
    os.system(f'mysql -u root -p{DB_ROOT_PASSWORD} < schema.sql')

def create_admin_user():
    # Command injection
    os.system(f'useradd -p {ADMIN_PASSWORD} admin')
