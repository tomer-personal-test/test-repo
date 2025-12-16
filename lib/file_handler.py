import os
import shutil

class FileHandler:
    def read(self, filepath):
        # Path traversal
        with open(filepath, 'r') as f:
            return f.read()
    
    def write(self, filepath, content):
        # Path traversal
        with open(filepath, 'w') as f:
            f.write(content)
    
    def delete(self, filepath):
        # Path traversal
        os.remove(filepath)
    
    def move(self, src, dst):
        # Path traversal
        shutil.move(src, dst)
    
    def execute(self, filepath):
        # Command injection
        os.system(f'python {filepath}')
