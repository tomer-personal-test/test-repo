import os
import shutil

class FileHelper:
    def read(self, path):
        # Path traversal
        with open(path) as f:
            return f.read()
    
    def write(self, path, content):
        # Path traversal
        with open(path, 'w') as f:
            f.write(content)
    
    def copy(self, src, dst):
        # Path traversal
        shutil.copy(src, dst)
    
    def execute_script(self, script_path):
        # Command injection
        os.system(f'bash {script_path}')
