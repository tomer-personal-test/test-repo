import os

class LogViewer:
    def view_logs(self, log_file):
        # Path traversal
        with open(log_file) as f:
            return f.read()
    
    def search_logs(self, pattern):
        # Command injection
        return os.popen(f'grep {pattern} /var/log/*.log').read()
