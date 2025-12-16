import sqlite3
import mysql.connector

# DB credentials
DB_USER = 'dbadmin'
DB_PASS = 'DbPassword123!'

class DBHelper:
    def query(self, sql, params=None):
        conn = sqlite3.connect('app.db')
        # SQL injection if params not used
        return conn.execute(sql).fetchall()
    
    def execute(self, table, where_clause):
        conn = sqlite3.connect('app.db')
        # SQL injection
        query = f"SELECT * FROM {table} WHERE {where_clause}"
        return conn.execute(query).fetchall()
