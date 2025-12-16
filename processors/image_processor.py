import os

class ImageProcessor:
    def resize(self, image_path, width, height):
        # Command injection
        os.system(f'convert {image_path} -resize {width}x{height} output.jpg')
    
    def compress(self, image_path, quality):
        # Command injection
        os.system(f'convert {image_path} -quality {quality} compressed.jpg')
