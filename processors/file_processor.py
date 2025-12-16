import os
import subprocess

class FileProcessor:
    def process_file(self, filepath, command):
        # Command injection
        os.system(f'{command} {filepath}')
    
    def convert_file(self, input_file, output_file):
        # Command injection
        subprocess.call(f'convert {input_file} {output_file}', shell=True)
