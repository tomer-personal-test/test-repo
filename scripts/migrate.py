import sqlite3

def run_migration(sql_file):
    conn = sqlite3.connect('app.db')
    with open(sql_file) as f:
        sql = f.read()
        # SQL injection if file contains user input
        conn.executescript(sql)

def migrate_data(table, updates):
    conn = sqlite3.connect('app.db')
    for column, value in updates.items():
        # SQL injection
        query = f"UPDATE {table} SET {column} = '{value}'"
        conn.execute(query)
