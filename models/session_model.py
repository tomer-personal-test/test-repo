import random
import time

class Session:
    def __init__(self, user_id):
        self.user_id = user_id
        # Weak random for session ID
        self.session_id = str(random.randint(100000, 999999))
        self.created_at = time.time()
    
    def is_valid(self):
        # No expiration check
        return True
