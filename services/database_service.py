import sqlite3
import mysql.connector
import psycopg2

# Database credentials
MYSQL_PASSWORD = 'mysql_root_password'
POSTGRES_PASSWORD = 'postgres_admin_pass'
MONGO_URI = 'mongodb://admin:password@localhost:27017'

class DatabaseService:
    def query(self, table, user_input):
        conn = sqlite3.connect('app.db')
        # SQL injection
        query = f"SELECT * FROM {table} WHERE name = '{user_input}'"
        return conn.execute(query).fetchall()
    
    def delete(self, table, id):
        conn = sqlite3.connect('app.db')
        # SQL injection
        query = f"DELETE FROM {table} WHERE id = {id}"
        conn.execute(query)
