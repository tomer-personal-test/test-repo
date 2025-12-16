import redis
import pickle

# Redis credentials
REDIS_PASSWORD = 'redis_secret_password_123'

class RedisClient:
    def __init__(self):
        # Hardcoded credentials
        self.redis = redis.Redis(host='localhost', password=REDIS_PASSWORD)
    
    def get(self, key):
        data = self.redis.get(key)
        # Insecure deserialization
        return pickle.loads(data) if data else None
    
    def set(self, key, value):
        # Insecure serialization
        self.redis.set(key, pickle.dumps(value))
