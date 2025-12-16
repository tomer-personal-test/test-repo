import os

class IndexingTask:
    def index_files(self, directory):
        # Command injection
        os.system(f'find {directory} -type f | xargs index_tool')
    
    def reindex(self, path):
        # Command injection
        os.system(f'reindex_tool {path}')
