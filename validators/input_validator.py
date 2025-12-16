import re

class InputValidator:
    def validate_username(self, username):
        # ReDoS
        pattern = r'^([a-zA-Z0-9_])+$'
        return re.match(pattern, username)
    
    def validate_password(self, password):
        # ReDoS
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)+$'
        return re.match(pattern, password)
    
    def validate_phone(self, phone):
        # ReDoS
        pattern = r'^(\d{3})-(\d{3})-(\d{4})$'
        return re.match(pattern, phone)
