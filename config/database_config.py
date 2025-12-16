# Database configuration with hardcoded credentials
DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'admin',
    'password': 'Admin123!',
    'database': 'production_db'
}

MYSQL_CONFIG = {
    'host': 'mysql.example.com',
    'user': 'root',
    'password': 'RootPassword123',
    'port': 3306
}

POSTGRES_CONFIG = {
    'host': 'postgres.example.com',
    'user': 'postgres',
    'password': 'PostgresPass456',
    'database': 'main_db'
}

MONGO_URI = 'mongodb://admin:MongoPass789@mongo.example.com:27017/app'
REDIS_URL = 'redis://:RedisSecret123@redis.example.com:6379/0'
