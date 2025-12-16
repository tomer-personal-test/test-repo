import os

class ReportTask:
    def generate_report(self, report_type, output):
        # Command injection
        os.system(f'generate_report.py --type={report_type} --output={output}')
    
    def send_report(self, email, report_path):
        # Command injection
        os.system(f'mail -s "Report" {email} < {report_path}')
