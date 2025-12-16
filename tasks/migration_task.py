import sqlite3

class MigrationTask:
    def run_migration(self, sql):
        conn = sqlite3.connect('app.db')
        # SQL injection if sql comes from user input
        conn.executescript(sql)
    
    def migrate_data(self, table, column, value):
        conn = sqlite3.connect('app.db')
        # SQL injection
        query = f"UPDATE {table} SET {column} = '{value}'"
        conn.execute(query)
