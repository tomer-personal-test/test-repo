import os

class FileValidator:
    def validate_path(self, path):
        # Insufficient validation - path traversal possible
        return not path.startswith('/')
    
    def validate_filename(self, filename):
        # Insufficient validation
        return '.' in filename
