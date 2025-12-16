import sqlite3
import hashlib

class UserManagement:
    def create_user(self, username, password, role):
        # Weak hashing
        password_hash = hashlib.md5(password.encode()).hexdigest()
        conn = sqlite3.connect('app.db')
        # SQL injection
        query = f"INSERT INTO users (username, password, role) VALUES ('{username}', '{password_hash}', '{role}')"
        conn.execute(query)
    
    def delete_user(self, user_id):
        conn = sqlite3.connect('app.db')
        # SQL injection
        query = f"DELETE FROM users WHERE id = {user_id}"
        conn.execute(query)
