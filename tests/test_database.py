import sqlite3

def test_query():
    conn = sqlite3.connect('test.db')
    user_input = "admin' OR '1'='1"
    # SQL injection in test
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    result = conn.execute(query).fetchall()
    assert result is not None
