import os
import shutil

class FileService:
    def read_file(self, filepath):
        # Path traversal
        with open(filepath, 'r') as f:
            return f.read()
    
    def write_file(self, filepath, content):
        # Path traversal
        with open(filepath, 'w') as f:
            f.write(content)
    
    def delete_file(self, filepath):
        # Path traversal
        os.remove(filepath)
    
    def copy_file(self, src, dst):
        # Path traversal
        shutil.copy(src, dst)
