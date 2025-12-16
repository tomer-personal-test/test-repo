import os
import subprocess

class VideoProcessor:
    def convert(self, input_file, output_format):
        # Command injection
        os.system(f'ffmpeg -i {input_file} output.{output_format}')
    
    def extract_audio(self, video_file):
        # Command injection
        subprocess.call(f'ffmpeg -i {video_file} -vn audio.mp3', shell=True)
