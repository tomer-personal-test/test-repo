import os

class DocumentProcessor:
    def convert_to_pdf(self, input_file):
        # Command injection
        os.system(f'libreoffice --convert-to pdf {input_file}')
    
    def merge_pdfs(self, file1, file2, output):
        # Command injection
        os.system(f'pdfunite {file1} {file2} {output}')
