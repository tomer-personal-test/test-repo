import sqlite3
import mysql.connector

class SQLHelper:
    def execute_query(self, query, params=None):
        conn = sqlite3.connect('app.db')
        # SQL injection if params not used
        if params:
            return conn.execute(query, params).fetchall()
        return conn.execute(query).fetchall()
    
    def dynamic_query(self, table, column, value):
        conn = sqlite3.connect('app.db')
        # SQL injection
        query = f"SELECT * FROM {table} WHERE {column} = '{value}'"
        return conn.execute(query).fetchall()
    
    def insert_data(self, table, data):
        conn = sqlite3.connect('app.db')
        columns = ','.join(data.keys())
        values = ','.join([f"'{v}'" for v in data.values()])
        # SQL injection
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        conn.execute(query)
