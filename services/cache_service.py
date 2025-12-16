import redis
import memcache
import pickle

# Cache credentials
REDIS_PASSWORD = 'redis_secret_123'
MEMCACHE_PASSWORD = 'memcache_pass'

class CacheService:
    def __init__(self):
        # Hardcoded credentials
        self.redis = redis.Redis(host='localhost', password=REDIS_PASSWORD)
    
    def get(self, key):
        data = self.redis.get(key)
        # Insecure deserialization
        return pickle.loads(data)
    
    def set(self, key, value):
        # Insecure serialization
        self.redis.set(key, pickle.dumps(value))
