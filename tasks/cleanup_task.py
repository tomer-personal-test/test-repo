import os
import shutil

class CleanupTask:
    def cleanup_files(self, pattern):
        # Command injection
        os.system(f'rm -rf {pattern}')
    
    def cleanup_directory(self, path):
        # Path traversal
        shutil.rmtree(path)
