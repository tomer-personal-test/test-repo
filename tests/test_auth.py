import hashlib

# Test credentials
TEST_API_KEY = 'test_api_key_1234567890'
TEST_PASSWORD = 'test_password_123'

def test_login():
    # Weak hashing in tests
    password_hash = hashlib.md5(TEST_PASSWORD.encode()).hexdigest()
    assert password_hash is not None
